from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>haha it was a prank, no crud project </h1>')