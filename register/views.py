
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django. http import HttpResponse
from django.contrib import admin
from django.urls import path
from register import views
from register.models import signin
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def intro(request):
    return render(request,'intro.html')

def service(request):
    return render(request,'service.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request,'login successfully')
            return redirect('/')
            
        else:
            messages.info(request,"invalid credential")
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def signin(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #Check for validation is working or not in username
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('signin.html')

        #Check for validation for username is only stored in alphabet letters
        if not username.isalpha():
            messages.error(request, "Username should only contain alphabet letters")
            return redirect('signin.html')
        #Check that password1 matches with password2
        if password != password2:
            messages.error(request, "Password does not matched")
            #return redirect('signin.html')

            user =  User.objects.create_user(username = username, password=password2, email = email, last_name = last_name, first_name = first_name )    
            user.save()
            messages.success(request, "Your account has been successfully created")
            return redirect('/')
        else:
            return HttpResponse('password not match')
    return render(request,'signin.html')


#User Logout 

def logout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "Successfully logged out")
        return redirect('/')
    return HttpResponse('logout')

#change Password

def changepassword(request):
    if request.method == 'POST':
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request, fm.user)
            return redirect('/')
    else:
        fm = PasswordChangeForm(user=request.user)
    return render(request, 'changepass.html', {'form': fm})
    