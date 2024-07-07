from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm # using UserCreationForm
# using my form withh more fields
from .forms import SignUpForm
from django.contrib import messages

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
