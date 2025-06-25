from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Wallet, Transaction
from django.contrib import messages
from user.models import signup
from decimal import Decimal


def wallet(request):
    username = request.session.get('username')
    if not username:
        return redirect('signin')

    user = signup.objects.get(username=username)
    wallet, _ = Wallet.objects.get_or_create(user=user)

    return render(request, 'wallet.html', {'wallet': wallet, 'username': username})


def balance(request):
    username = request.session.get('username')
    if not username:
        return redirect('signin')

    user = signup.objects.get(username=username)
    wallet, _ = Wallet.objects.get_or_create(user=user)

    return render(request, 'balance.html', {'balance': wallet.balance, 'username': username})


def history(request):
    username = request.session.get('username')
    if not username:
        return redirect('signin')

    user = signup.objects.get(username=username)
    transactions = Transaction.objects.filter(user=user).order_by('-timestamp')

    return render(request, 'history.html', {'transactions': transactions, 'username': username})


def Payment(request):
    username = request.session.get('username')
    if not username:
        return redirect('signin')

    return render(request, 'payment.html', {'username': username})


def sendmoney(request):
    username = request.session.get('username')
    if not username:
        return redirect('signin')

    user = signup.objects.get(username=username)
    wallet, _ = Wallet.objects.get_or_create(user=user)

    if request.method == "POST":
        amount = Decimal(request.POST.get('amount'))
        products = request.POST.get('products', '')

        if wallet.balance >= amount:
            wallet.balance -= amount
            wallet.save()

            Transaction.objects.create(
                user=user,
                transaction_type='SEND',
                amount=amount,
                product_names=products,
                description="Money sent"
            )
            messages.success(request, "Money sent successfully!")
            return redirect('wallet')
        else:
            messages.error(request, "Insufficient balance!")

    return render(request, 'sendmoney.html', {'username': username})


def Addmoney(request):
    username = request.session.get('username')
    if not username:
        return redirect('signin')

    user = signup.objects.get(username=username)
    wallet, _ = Wallet.objects.get_or_create(user=user)

    if request.method == "POST":
        amount = Decimal(request.POST.get('amount'))
        products = request.POST.get('products', '')

        wallet.balance += amount
        wallet.save()

        Transaction.objects.create(
            user=user,
            transaction_type='ADD',
            amount=amount,
            product_names=products,
            description="Money added"
        )
        messages.success(request, "Money added successfully!")
        return redirect('wallet')

    return render(request, 'Addmoney.html', {'username': username})


def edit_transaction(request, txn_id):
    username = request.session.get('username')
    if not username:
        return redirect('signin')

    user = signup.objects.get(username=username)
    wallet, _ = Wallet.objects.get_or_create(user=user)
    transaction = Transaction.objects.get(id=txn_id, user=user)

    if request.method == 'POST':
        new_amount = Decimal(request.POST.get('amount'))
        new_products = request.POST.get('products')
        old_amount = transaction.amount

        # Adjust wallet balance before updating
        if transaction.transaction_type == 'ADD':
            wallet.balance -= old_amount
            wallet.balance += new_amount
        elif transaction.transaction_type == 'SEND':
            wallet.balance += old_amount
            if wallet.balance >= new_amount:
                wallet.balance -= new_amount
            else:
                messages.error(request, "Insufficient balance for this update!")
                return redirect('edit_transaction', txn_id=txn_id)

        wallet.save()

        transaction.amount = new_amount
        transaction.product_names = new_products
        transaction.save()

        messages.success(request, "Transaction updated successfully!")
        return redirect('history')

    return render(request, 'edit_transaction.html', {'transaction': transaction, 'username': username})

def delete_transaction(request, txn_id):
    username = request.session.get('username')
    if not username:
        return redirect('signin')

    user = signup.objects.get(username=username)
    wallet, _ = Wallet.objects.get_or_create(user=user)
    transaction = Transaction.objects.get(id=txn_id, user=user)

    # Adjust wallet balance
    if transaction.transaction_type == 'ADD':
        wallet.balance -= transaction.amount
    elif transaction.transaction_type == 'SEND':
        wallet.balance += transaction.amount

    wallet.save()
    transaction.delete()

    messages.success(request, "Transaction deleted successfully!")
    return redirect('history')
