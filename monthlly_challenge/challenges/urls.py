from django.urls import path
from . import views

urlpatterns = [
    # path('january' , views.january , name="january"),
    # path('february' , views.february , name="february"),
    # # path('march' , views.march , name="march")
    path("",views.index),
    path("<int:id>",views.monthly_challege_by_id,name="monthly_id"),
    path("<str:month>",views.monthly_challege,name="monthly_challege")
]