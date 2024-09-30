from django.shortcuts import render
from .models import Student
from django.db.models import Avg, Sum, Min, Max, Count

def home(request):
    student_data = Student.objects.all()
    average = student_data.aggregate(Avg('marks'))
    summation = student_data.aggregate(Sum('marks'))
    minimum = student_data.aggregate(Min('marks'))
    maximum = student_data.aggregate(Max('marks'))
    totalcount = student_data.aggregate(Count('marks'))

    context = {
        'students': student_data,
        'average': average,
        'summation': summation,
        'minimum': minimum,
        'maximum': maximum,
        'totalcount': totalcount,
    }

    return render(request, 'school/home.html', context)
