from django.shortcuts import render
from .models import Student, ProxyStudent
# Create your views here.

def home(request):
    # get data from 1 to 9
    # student_data = Student.objects.all()
    student_data = ProxyStudent.students.get_stu_roll_range(1,9)
    return render(request, 'school/home.html', {'students': student_data})