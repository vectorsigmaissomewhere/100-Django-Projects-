from django.shortcuts import render,redirect, HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm # using UserCreationForm
# using my form with more fields
from .forms import SignUpForm # from forms.py
from .forms import EditUserProfileForm # from forms.py to view only few data in profile.html
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm # pre-build form to change password with old password
from django.contrib.auth.forms import SetPasswordForm # password change form to change password without old password
from django.contrib.auth.forms import UserChangeForm # I think it gives all information of user
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash # maintains session 


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

# use this function view if you want to use your forms.py to include more fields  
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
    if request.user.is_authenticated: # means user who have not logged in cannot see the profile page
        if request.method == "POST":
            fm = EditUserProfileForm(request.POST, instance = request.user)
            if fm.is_valid():
                messages.success(request, 'Profile Updated!!!')
                fm.save()
        else:
            # if you use UserChangeForm instead of EditUserProfileForm all the data will be visible 
            fm = EditUserProfileForm(instance=request.user) # form to show all the user detail
        return render(request, 'enroll/profile.html', {'name': request.user,'form':fm})
    else:
        return HttpResponseRedirect('/login/')

# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

# views to change password with old password 
def user_change_pass(request):
    # I don't want to see the change password template when user is logged out
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user) # session is not maintained and it is logging out so using this function
                messages.success(request,'Password Changed Successfully')
                return HttpResponseRedirect('/profile/')    
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'enroll/changepass.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')

# change password without old password
def user_change_pass1(request):
    # I don't want to see the change password template when user is logged out
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = SetPasswordForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user) # session is not maintained and it is logging out so using this function
                messages.success(request,'Password Changed Successfully')
                return HttpResponseRedirect('/profile/')    
        else:
            fm = SetPasswordForm(user=request.user)
        return render(request, 'enroll/changepass1.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')