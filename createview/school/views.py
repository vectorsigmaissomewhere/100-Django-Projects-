from django.shortcuts import render
from django.views.generic.edit import CreateView 
from .models import Student 
from django.views.generic.base import TemplateView 
from django.views.generic.detail import DetailView 
from django import forms 

from .forms import StudentForm

# data will get saved 
class StudentCreateView(CreateView):
    model = Student 
    fields = ['name', 'email', 'password']
    # success_url = '/create/' # after the data is saved go to this url 
    success_url = '/thanks/'
    # template_name = 'school/sform.html' # custom form 

    # adding class to the form template html 
    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs={'class':'myclass'})
        form.fields['email'].widget = forms.TextInput(attrs={'class':'myclass'})
        form.fields['password'].widget = forms.PasswordInput(attrs={'class':'mypass'})
        return form

class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'

class StudentDetailView(DetailView):
    model = Student 


# This is send model create view that is related with forms.py
class StudentTwoCreateView(CreateView):
    form_class = StudentForm
    template_name = 'school/student_form.html'
    success_url = '/thanks/'
