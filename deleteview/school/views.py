from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from .models import Student 
from django.views.generic.base import TemplateView 
from django import forms

from .forms import StudentForm

"""Not working with forms.py"""
# Create your views here.
class StudentCreateView(CreateView):
    model = Student 
    fields = ['name', 'email', 'password']
    success_url = '/thanks/'
    template_name = 'school/student_form.html'

    # adding classes in form 
    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs={'class':'myclass'})
        form.fields['password'].widget = forms.PasswordInput(attrs={'class':'mypass'})
        return form 


class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'

class StudentUpdateView(UpdateView):
    model = Student 
    fields = ['name', 'email', 'password']
    success_url = '/thanksupdate/'

    # adding classes in form 
    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs={'class':'myclass'})
        form.fields['password'].widget = forms.PasswordInput(attrs={'class':'mypass'})
        return form 

class ThanksUpdateView(TemplateView):
    template_name = 'school/thanksupdate.html'



"""Now working with forms.py"""
class StudentCreateView2(CreateView):
    form_class = StudentForm 
    template_name = 'school/student_form.html'
    success_url = '/thanks/'

class StudentUpdateView2(UpdateView):
    model = Student
    form_class = StudentForm 
    template_name = 'school/student_form.html'
    success_url = '/thanksupdate/'


class StudentDeleteView(DeleteView):
    model = Student 
    success_url = '/create/'

# Delete with customtemplate
class StudentCustomDeleteView(DeleteView):
    model = Student 
    success_url = '/create/'
    template_name = 'school/studel.html'
