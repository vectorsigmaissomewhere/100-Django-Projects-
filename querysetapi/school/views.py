from django.shortcuts import render
from .models import Student, Teacher
from django.db.models import Q

# get all models objects
def queryall(request):
    student_data = Student.objects.all()
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query) # generate sql query
    return render(request, 'school/home.html', {'students': student_data})

# filter model object attribute
def queryfilter(request):
    student_data = Student.objects.filter(marks=90)
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query) # generate sql query
    return render(request, 'school/home.html', {'students': student_data})

# filter model object attribute 
def queryexclude(request):
    student_data = Student.objects.exclude(marks=90)
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query) # generate sql query
    return render(request, 'school/home.html', {'students': student_data})

# queryset in ascending order by looking unicode means 
# if there are three city Akabare, Biratnagar, akabare
# when you run the query you will be getting the model object in 
# "Akabare, Biratnagr, akabare " order instead it should be 
# "AKabare, akabare, Biratnagar"
def queryascendingorderby(request):
    student_data = Student.objects.order_by('city')
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query) # generate sql query
    return render(request, 'school/home.html', {'students': student_data})

# queryset in descending order
def querydescendingorderby(request):
    student_data = Student.objects.order_by('-city')
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query) # generate sql query
    return render(request, 'school/home.html', {'students': student_data})

# random queryset, each time you call this method you get the different order query object
def queryrandom(request):
    student_data = Student.objects.order_by('?')
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query) # generate sql query
    return render(request, 'school/home.html', {'students': student_data})

# reverse(), model objects in reverse order
def queryreverse(request):
    student_data = Student.objects.order_by('id').reverse()
    #student_data = Student.objects.order_by('id').reverse()[:2] # get last 3 model objects
    #student_data = Student.objects.order_by('id').reverse()[0:2] # get last 3 model objects
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query) # generate sql query
    return render(request, 'school/home.html', {'students': student_data})

# values() , get model objects in list of dictionaries 
def queryvalues(request):
    # student_data = Student.objects.values()
    student_data = Student.objects.values('name', 'city') # if I need only name and city
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query) # generate sql query
    return render(request, 'school/home.html', {'students': student_data})

# values_list() no values is associated with id, so you won't be able to see the data this way
def queryvalueslist(request):
    # student_data = Student.objects.values_list() # make named=True to see data
    student_data = Student.objects.values_list('id', 'name', named=True) # if i need only id and names 
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query) # generate sql query
    return render(request, 'school/home.html', {'students': student_data})

# using() method
def using(request):
    student_data = Student.objects.using('default')
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query) # generate sql query
    return render(request, 'school/home.html', {'students': student_data})

# dates() method
def querydates(request):
    # by default in ascending order
    student_data = Student.objects.dates('pass_date', 'month') # values in tuple so we are unable to see, make named = True to view data
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query) # generate sql query
    return render(request, 'school/home.html', {'students': student_data})


# union() method
def queryunion(request):
    qs1 = Student.objects.values_list('id', 'name', named=True)
    qs2 = Teacher.objects.values_list('id', 'name', named=True)
    student_data = qs2.union(qs1)
    # student_data = qs2.union(qs1, all=True) # if you want duplicates
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query) # generate sql query
    return render(request, 'school/home.html', {'students': student_data})

# intersection() method
def queryintersection(request):
    qs1 = Student.objects.values_list('id', 'name', named=True)
    qs2 = Teacher.objects.values_list('id', 'name', named=True)
    student_data = qs2.intersection(qs1)
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query) # generate sql query
    return render(request, 'school/home.html', {'students': student_data})

# difference() method
def querydifference(request):
    qs1 = Student.objects.values_list('id', 'name', named=True)
    qs2 = Teacher.objects.values_list('id', 'name', named=True)
    student_data = qs2.difference(qs1)
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query) # generate sql query
    return render(request, 'school/home.html', {'students': student_data})

def andoperator(request):
    student_data = Student.objects.filter(id=4) & Student.objects.filter(roll=104)
    # student_data = Student.objects.filter(id=4, roll=104) # second way 
    # student_data = Student.objects.filter(Q(id=6) & Q(roll=106)) # third way 
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query) # generate sql query
    return render(request, 'school/home.html', {'students': student_data})

def oroperator(request):
    student_data = Student.objects.filter(id=4) | Student.objects.filter(roll=103)
    # student_data = Student.objects.filter(Q(id=4) | Q(roll=103)) # second way  
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query) # generate sql query
    return render(request, 'school/home.html', {'students': student_data})

