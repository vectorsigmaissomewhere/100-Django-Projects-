from django.shortcuts import render
from django.views.decorators.cache import cache_page # used to cache a view

# Create your views here.
#@cache_page(60) # helps to cache this view within one minute you will get the same data fro 1 minute
def home(request):
    return render(request, 'enroll/course.html')

def contact(request):
    return render(request, 'enroll/contact.html')

