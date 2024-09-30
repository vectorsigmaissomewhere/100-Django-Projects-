from django.shortcuts import render
from .models import Student
from django.db.models import Q

def home(request):
    # student_data = Student.objects.all()[:3] # first three data
    #student_data = Student.objects.all()[1:3] # data from 2 to 3
    student_data = Student.objects.all()[:4:2] # skipping 2 items
    print("Return: ", student_data)
    print()
    #print("SQL Query:", student_data.query)
    return render(request, 'school/home.html',{'students':student_data})

