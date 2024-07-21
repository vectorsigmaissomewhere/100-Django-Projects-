from django.shortcuts import render
from datetime import datetime, timedelta

# this the code to set cookies
def setcookie(request):
    response = render(request, 'student/setcookie.html') # renders setcookie.html when cookie is set
    """set cookies"""
    #response.set_cookie('name', 'sonam')
    # response.set_cookie('name', 'sonam', max_age=120) # after 120 second the cookie will expire
    # response.set_cookie('name', 'sonam', expires=datetime.utcnow()+timedelta(days=2)) # the cookie will expire after 2 days 
    """set signed cookies"""
    response.set_signed_cookie('name', 'sonam',salt='nm', expires=datetime.utcnow()+timedelta(days=2)) 
    return response

# get the cookie value
def getcookie(request):
    """get cookies """
    #name = request.COOKIES['name']
    #name = request.COOKIES.get('name')
    # name = request.COOKIES.get('name', "Guest") # if name key is not available it will show guest
    """get signed cookies"""
    name = request.get_signed_cookie('name',default="Guest", salt='nm')
    return render(request, 'student/getcookie.html', {'name':name}) #sending name to the getcookie.html 

# delete the cookie value
def delcookie(request):
    response = render(request, 'student/delcookie.html') # render delcookie to delete cookie
    response.delete_cookie('name') 
    return response


