from django.shortcuts import render
from .models import Student
from django.db.models import Q

def home(request):
    # student_data = Student.objects.filter(Q(id=4) & Q(roll=104)) # filter whose id is 4 or roll is 104
    # student_data = Student.objects.filter(Q(id=4) | Q(roll=103)) # filter whose id is 4 or roll is 103
    student_data = Student.objects.filter(~Q(id=6)) # student data whose id is not 6 
    print("Return: ", student_data)
    print()
    print("SQL Query:", student_data.query)
    return render(request, 'school/home.html',{'students':student_data})

