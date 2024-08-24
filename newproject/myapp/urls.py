from django.urls import path
from .views import *
urlpatterns = [
    path('createform',createform,name='createform'),
    path('getdata/',getdata,name="getdata"),
     path('editdata/<id>',editdata,name="editdata"),
     path('deletedata/<id>',deletedata,name="deletedata"),
]
