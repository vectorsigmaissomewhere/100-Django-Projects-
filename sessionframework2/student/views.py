from django.shortcuts import render

def setsession(request):
    request.session['name'] = 'Sonam'
    request.session['lname'] = 'Ronaldo'
    return render(request, 'student/setsession.html')

def getsession(request):
    name = request.session.get('name')
    lname = request.session.get('lname')
    keys = request.session.keys()
    items = request.session.items()
    age = request.session.setdefault('age', '26')
    return render(request, 'student/getsession.html', {'name': name,'lname': lname, 'keys': keys, 'items': items, 'age': age})

def delsession(request):
    if 'name' in request.session:
        del request.session['name']
        del request.session['lname']
        # you can use sesion.flush() to remove all the sessions can delete all the session in single line of code 
        # request.session.flush()
    return render(request, 'student/delsession.html')

