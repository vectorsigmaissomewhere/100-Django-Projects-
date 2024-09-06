from django.shortcuts import render, HttpResponse
# for generating exception
def home(request):
    a = 10/0
    return HttpResponse("Hello")