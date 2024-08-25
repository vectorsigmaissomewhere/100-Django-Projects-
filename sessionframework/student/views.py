from django.shortcuts import render

def setsession(request):
    request.session['name'] = 'Sonam'
    request.session['lname'] = 'rathore'
    return render(request, 'student/setsession.html')

def getsession(request):
    # name = request.session['name']
    name = request.session.get('name', default='Guest')
    lname = request.session.get('lname', default='Guest')
    return render(request, 'student/getsession.html', {'name': name, 'lname':lname})

def delsession(request):
    if 'name' in request.session:
        del request.session['name']
        del request.session['lname']
    return render(request, 'student/delsession.html')

