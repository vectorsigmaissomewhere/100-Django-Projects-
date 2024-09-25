from django.shortcuts import render
from .models import Student

def home(request):
    student_data = Student.objects.get(pk=1)
    print("Return:", student_data)
    return render(request, 'school/home.html', {'student':student_data})

def firstmethod(request):
    # student_data = Student.objects.first()
    student_data = Student.objects.order_by('name').first()
    print("Return:", student_data)
    return render(request, 'school/home.html', {'student':student_data})

def lastmethod(request):
    student_data = Student.objects.last()
    # student_data = Student.objects.order_by('name').last()
    print("Return:", student_data)
    return render(request, 'school/home.html', {'student':student_data})

def latestmethod(request):
    # latest product according to date
    student_data = Student.objects.latest('pass_date')
    print("Return:", student_data)
    return render(request, 'school/home.html', {'student':student_data})

def earliestmethod(request):
    # earliest product according to date
    student_data = Student.objects.earliest('pass_date')
    print("Return:", student_data)
    return render(request, 'school/home.html', {'student':student_data})

# exists method returns True if an object exists
def existmethod(request):
    student_data = Student.objects.all()
    print(student_data.exists())
    print("Return:", student_data)
    return render(request, 'school/home.html', {'student':student_data})

# create method, creates and saved the model object
def createmethod(request):
    student_data = Student.objects.create(name='Sameer', roll=114, city='Bokaro', marks=60, pass_date='2020-5-4')
    print("Return:", student_data)
    return render(request, 'school/home.html', {'student':student_data})

# get_or_create method if there is value get if not create it 
def get_or_create(request):
    student_data, created = Student.objects.get_or_create(name='Anisha', roll=115, city='Bokaro', marks=60, pass_date='2020-5-4')
    print(created)
    print("Return:", student_data)
    return render(request, 'school/home.html', {'student':student_data})

# update method
def update(request):
    # student_data = Student.objects.filter(id=5).update(name='Manisha', marks=80)
    student_data = Student.objects.filter(marks=90).update(city='Delhi')
    print("Return:", student_data)
    return render(request, 'school/home.html', {'student':student_data})

# update or create method
def update_or_create(request):
    student_data, created = Student.objects.update_or_create(id=5,name='Sameer', defaults={'name':'Ronaldo'})
    print(created)
    print("Return:", student_data)
    return render(request, 'school/home.html', {'student':student_data})

# bulk_create() method
def bulk_create(request):
    objs = [
    Student(name='Sonal', roll=116, city='Dhanbad', marks=90, pass_date='2020-5-4'),
    Student(name='Kunal', roll=117, city='Dumka', marks=90, pass_date='2020-5-7'),
    Student(name='Anisa', roll=118, city='Giridih', marks=80, pass_date='2020-5-9')
]
    student_data = Student.objects.bulk_create(objs)
    print("Return:", student_data)
    return render(request, 'school/home.html', {'student':student_data})

def bulk_update(request):
    all_student_data = Student.objects.all()
    for stu in all_student_data:
        stu.city = 'Bhel'
    student_data = Student.objects.bulk_update(all_student_data, ['city'])
    print("Return:", student_data)
    return render(request, 'school/home.html', {'student':student_data})

def in_bulk(request):
    # student_data = Student.objects.in_bulk([1,2])
    # student_data = Student.objects.in_bulk([]) # this gives empty dictionary
    student_data = Student.objects.in_bulk() # this gives all model object
    #print(student_data[1].name) # return a particular model value
    print(student_data)
    print("Return:", student_data)
    return render(request, 'school/home.html', {'student':student_data})

def deletemethod(request):
    student_data = Student.objects.get(pk=8).delete()
    # student_data = Student.objects.filter(pk=8).delete()
    # student_data = Student.objects.all().delete() # delete all model objects
    print(student_data)
    print("Return:", student_data)
    return render(request, 'school/home.html', {'student':student_data})

def countmethod(request):
    student_data = Student.objects.all()
    print(student_data.count())
    print(student_data)
    print("Return:", student_data)
    return render(request, 'school/home.html', {'student':student_data})

def explainmethod(request):
    student_data = Student.objects.all()
    print(Student.objects.all().explain)
    print(student_data)
    print("Return:", student_data)
    return render(request, 'school/home.html', {'student':student_data})

    
    