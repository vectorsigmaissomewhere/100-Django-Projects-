# why to create forms.py because we need other fields like first name last name and email

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm # use to display all the info of user 
from django import forms

# extending the form 
class SignUpForm(UserCreationForm):
    # customize UserCreationForm label in this place
    # there are password1 and password2 in UserCreationForm 
    # Changing label of password2 
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email': 'Email'} # changing the label name 

    
# using UserChangeForm and show only the data that we need to show
class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User # all the data coming from User model so using User here
        fields = ['username','first_name','last_name','email','date_joined','last_login']
        labels = {'email':'Email'} # changing the label name of email
