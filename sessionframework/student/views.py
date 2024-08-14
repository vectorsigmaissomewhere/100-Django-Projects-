from django.shortcuts import render

def setsession(request):
    request.session['name'] = 'Sonam'
    return render(request, 'student/setsession.html')