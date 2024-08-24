from django.shortcuts import render, redirect
from .models import *


# Create your views here.

def createform(request):
    if request.method == "POST":
       name = request.POST.get('name')
       email =  request.POST.get('email')
       number = request.POST.get('number')
       users = Users(name=name,email=email,number=number)
       users.save()
       
       return render(request,'myapp/createform.html',{'message':"user added successfully"})
        
    return render(request,'myapp/createform.html')

def getdata(request):
    users = Users.objects.all()
    return render(request,'myapp/getdata.html',{"users":users})


def editdata(request,id):
    user = Users.objects.get(id=id)
    if request.method =="POST":
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.number = request.POST['number']
        user.save()
        return redirect('getdata')
    return render(request,'myapp/editdata.html',{'user':user})

def deletedata(request,id):
    if request.method =="POST":
        user = Users.objects.get(id=id)    
        user.delete()   
        return redirect('getdata')
    return render(request,'myapp/getdata.html')
