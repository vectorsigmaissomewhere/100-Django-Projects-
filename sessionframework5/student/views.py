from django.shortcuts import render

def setsession(request):
    request.session['name'] = 'Sonam'
    request.session.set_expiry(600) # expiry date set for 30 seconds
    # request.session.set_expiry(0) # expires when the browser is closed 
    return render(request, 'student/setsession.html')

def getsession(request):
    name = request.session['name']
    return render(request, 'student/getsession.html', {'name': name})

def delsession(request):
    request.session.flush()
    request.session.clear_expired() # remove the session from the database
    return render(request, 'student/delsession.html')

