from django.shortcuts import render
from .models import Student
from datetime import date, time
# Create your views here.

def home(request):
    student_data = Student.objects.all()
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})

# exact lookup
# getting all the data with name ali 
# it is case sensitive
def exact(request):
    student_data = Student.objects.filter(name__exact='Ali') 
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})

# iexact works same as exact but it is case insensitive
def iexact(request):
    student_data = Student.objects.filter(name__iexact='ali') 
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})

# contains lookup , is there any name that contain the given value
def contains(request):
    student_data = Student.objects.filter(city__contains='I') 
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})

# icontains lookup 
def icontains(request):
    student_data = Student.objects.filter(city__icontains='I') 
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})

# in lookup, filter the id where it is 1 , 2
def inlookup(request):
    student_data = Student.objects.filter(id__in=[1,2]) 
    # student_data = Student.objects.filter(marks__in=[60,70])
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})

# gt greater than lookup
def greaterthan(request):
    student_data = Student.objects.filter(marks__gt=70) 
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})

# gte greater than and equal lookup
def greaterthanequal(request):
    student_data = Student.objects.filter(marks__gte=70) 
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})

# lt less than lookup
def lessthan(request):
    student_data = Student.objects.filter(marks__lt=70) 
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})

# lte less than equal lookup, now you will even get 70
def lessthanequal(request):
    student_data = Student.objects.filter(marks__lte=70) 
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})

# startswith # case sensitive
def startswith(request):
    student_data = Student.objects.filter(name__startswith='s') 
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})
    
# istartswith # case insensitive
def istartswith(request):
    student_data = Student.objects.filter(name__istartswith='S') 
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})

# endswith # case senstitive
def endswith(request):
    student_data = Student.objects.filter(name__endswith='l') 
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})

# iendswith # case sensitive
def iendswith(request):
    student_data = Student.objects.filter(name__iendswith='L') 
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})

# range, from this range to that range
def range(request):
    student_data = Student.objects.filter(passdate__range=('2020-01-01', '2024-05-30'))
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})

# date lookup
def datelookup(request):
    student_data = Student.objects.filter(admdatetime__date=date(2024, 5, 8))
    # you can use anylookup like for example 
    # student_data = Student.objects.filter(admdatetime__date__gt=date(2024, 5, 8))
    # student_data = Student.objects.filter(passdate__year=2020)
    # student_data = Student.objects.filter(passdate__year__gt=2019) # greater than 
    # student_data = Student.objects.filter(passdate__year__gte=2020) # greater than and equal
    # student_data = Student.objects.filter(passdate__month=4) # get all april data
    # student_data = Student.objects.filter(passdate__month__gt=4) # month greater than 4
    # student_data = Student.objects.filter(passdate__month__gte=4) # month greater and equal to 4
    # student_data = Student.objects.filter(passdate__day=2) # day equal to 2
    # student_data = Student.objects.filter(passdate__day__gt=2)
    # student_data = Student.objects.filter(passdate__day__gte=2)
    # student_data = Student.objects.filter(passdate__week=23)
    # student_data = Student.objects.filter(passdate__week__gt=14) 
    # student_data = Student.objects.filter(passdate__weeek_day=1) # data where there is sunday 
    # student_data = Student.objects.filter(passdate__week_day__gt=5)
    # student_data = Student.objects.filter(passdate__quarter=2) # first quarter january, feburary, march , second quarter april, may, june
    # student_data = Student.objects.filter(admdatetime__time__gt=time(6,30)) # data after 6:30
    # student_data = Student.objects.filter(admdatetime__hour__gt=5)
    # student_data = Student.objects.filter(admdatetime__minute__gt=26)
    # student_data = Student.objects.filter(admdatetime__second__gt=20)
    # student_data = Student.objects.filter(roll__isnull=True) # model object where the roll column is null
    

    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})




