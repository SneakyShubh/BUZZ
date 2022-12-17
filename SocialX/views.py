from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    return render(request,'base.html')
@csrf_exempt
def profile_pic(request):
    if request.method == "POST":
        file = request.POST.get('filename')
        return render(request,'c2.html',context={'f1':file})
def logout(request):
    messages.success(request,"Successfully Logged Out!")
    return render(request,'base.html')
@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        used = authenticate(username= username, password = pass1)
        fname = used.first_name
        username = used.username
        last_name = used.last_name
        email = used.email
        if used is not None:
            auth_login(request,used)
            messages.success(request,"Your Account has been created successfully !!")
            return render(request,'b2.html',context = {'fname':fname,'username':username})
    return render(request,'login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        lname = request.POST.get('lname')
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your Account has been created successfully !!")
        return redirect('../login/')
    return render(request,'signup.html')

def about(request):
    return render(request,'base.html')    