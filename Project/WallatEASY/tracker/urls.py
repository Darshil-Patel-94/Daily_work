from django.urls import path
from . import views

urlpatterns = [
    path('wallet/', views.wallet, name='wallet'),
    path('history/', views.history, name='history'),
    path('balance/', views.balance, name='balance'),
    path('Payment/', views.Payment, name='Payment'),
    path('sendmoney/', views.sendmoney, name='sendmoney'),
    path('Addmoney/', views.Addmoney, name='Addmoney'),
    path('edit_transaction/<int:txn_id>/', views.edit_transaction, name='edit_transaction'),
    path('delete_transaction/<int:txn_id>/', views.delete_transaction, name='delete_transaction'),
]