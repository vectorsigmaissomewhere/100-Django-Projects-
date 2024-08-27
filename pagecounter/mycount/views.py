from django.shortcuts import render

# Create your views here.
def home(request):
    ct = request.session.get('count', 0) # if there is count then return the value
    newcount = ct + 1
    request.session['count'] = newcount
    return render(request, 'mycount/home.html', {'c': newcount})