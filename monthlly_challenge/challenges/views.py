from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse

challege_months ={
    "january": "Start Learning the Django Basics for this month understand the things which is the Django using the for basics!!",
    "fabruary": "For this month Doing the Some practicals of the basic functions like views , urls , models and apps!",
    "march": "Experiment that all the Basic implemented things that work the correctlly or not!",
    "april": "Understand the Models and relation of the models",
    "may": "Understand the different databases supported and knew the syntax",
    "june": "start the one project on the django",
    "july": "understadn the probelms and try to solve it!!",
    "augest": "this is the month where you can show your project!",
    "september": "You are become the intemediate coder in djago",
    "october": "Search for real world problem",
    "november": "You find the project and start th working on it",
    "december": "Finally You become the pro!!"
}


# def january(request):
#     return HttpResponse("Start Learning the Django Basics for this month understand the things which is the Django using the for basics!! ")

# def february(request):
#     return HttpResponse("For this month Doing the Some practicals of the basic functions like views , urls , models and apps!")

# def march(request):
#     return HttpResponse("Experiment that all the Basic implemented things that work the correctlly or not!")

def index(request):
    list_item = ""
    months = list(challege_months.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("monthly_challege",args=[month])
        list_item += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    
    response_data = f"<h1>{list_item}</h1>"
    return HttpResponse(response_data)


def monthly_challege_by_id(request , id):
    ids =   list(challege_months.keys())
    if id > len(ids):
        return HttpResponseNotFound("Invalid Month!!")
    forwarded_id = ids[id]
    redirected_path = reverse("monthly_challege",args=[forwarded_id])
    return HttpResponseRedirect(redirected_path)

def monthly_challege(request , month):
    try:
        challenge_task = challege_months[month]
    except:
        return HttpResponseNotFound("This Month is not Found!!")
    return HttpResponse(challenge_task)