from django.shortcuts import render,redirect, HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm # using UserCreationForm
# using my form with more fields
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# use this function view if you need only username and password
"""
def sign_up(request):
    if request.method == "POST":
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = UserCreationForm() # a blank form object
    return render(request, 'enroll/signup.html',{'form':fm}) # rendering the fm template in signup.html
"""

# use this function view if you want to use your forms 
def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,"Account created successfully !!")
            fm.save()
            redirect('/signup/')
    else:
        fm = SignUpForm() # a blank form object
    return render(request, 'enroll/signup.html',{'form':fm}) # rendering the fm template in signup.html


# making a login view function
def user_login(request):
    # if someone is already authenticated i don't need to login
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully !!')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'enroll/userlogin.html', {'form': fm})
    else:
        return HttpResponseRedirect('/profile/')
    
    
# Profile
def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'enroll/profile.html', {'name': request.user})
    else:
        return HttpResponseRedirect('/login/')

# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

