from django.http import HttpResponse
from django.shortcuts import redirect, render
from . models import Room
from . models import explore
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def index(request):
    d=Room.objects.all()
    return render(request,'index.html',{'dest':d})
def signup(request):
    return render(request,'usersignup.html')   
def Explore(request):
    m=explore.objects.all()
    return render(request,'explore.html',{'exp':m})     
def signin(request):
    if request.method=="POST":
        username=request.POST['name']
        email=request.POST['email']
        pass2=request.POST['password2']
        pass1=request.POST['password1']
        p_no=request.POST['p_no']
        myuser=User.objects.create(username=username,email=email,password=pass1)
        myuser.save()
        return HttpResponse("hai")
def code(request):
    pass        