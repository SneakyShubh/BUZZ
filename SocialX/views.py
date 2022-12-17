from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.views.decorators.csrf import csrf_exempt
from .form import ImageForm
from .models import Profile_Pic
# Create your views here.
def index(request):
    return render(request,'base.html')


def logout(request):
    messages.success(request,"Successfully Logged Out!")
    return render(request,'base.html')
@csrf_exempt
def login(request):
    if request.method == "POST" and request.POST.get('username') and request.POST.get('pass1'):
        
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        used = authenticate(username= username, password = pass1)
        fname = used.first_name
        username = used.username
        last_name = used.last_name
        email = used.email
        kl = Profile_Pic.objects.all()
        jk = True
        for x in kl :
            if x.username == username:
                obj = x
                jk = False 
                break

        
        if used is not None:
            auth_login(request,used)
            intaial_data = {
            'username': used.username
            }
            messages.success(request,"Your Account has been created successfully !!")
            form1=ImageForm(initial=intaial_data)
            field = form1.fields['username']
            field.widget = field.hidden_widget()
            if jk:
                return render(request,'b2.html',context = {'fname':fname,'username':username,'form1':form1,'sed':True}) 
            else :
                return render(request,'b2.html',context = {'fname':fname,'username':username,'form1':form1,'sed':False,'obj':obj}) 
    if request.method == "POST":
        form = ImageForm(data=request.POST,files=request.FILES)
        

        if form.is_valid():
            # kl = Profile_Pic.objects.all()
            form.save()
            obj = form.instance
            Profile_Pic.objects.filter(username=obj.username).delete()
            form.save()

            

            k = User.objects.all()
            for x in k:
                if x.username == obj.username:
                    fg = x
                    break
            fname= fg.first_name
            username= fg.username
            intaial_data = {
            'username': username
                }
            form2 = ImageForm(initial=intaial_data) 
            field = form2.fields['username']
            field.widget = field.hidden_widget()
            return render(request,"b2.html",context = {'fname':fname,'username':username,'form1':form2,'obj':obj})
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