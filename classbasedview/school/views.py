from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ContactForm
from django.http import HttpResponse

# Function Based View
def myview(request):
    return HttpResponse('<h1>Function Based View</h1>')

# Class Based View
class MyView(View):
    name = 'Ronaldo'
    def get(self, request):
        return HttpResponse(self.name)

# inheriting MyView class 
class MyViewChild(MyView):
    def get(self, request):
        return HttpResponse("This is sub class "+self.name)
    
# function based view 
def homefun(request):
    return render(request, 'school/home.html')

# class based view 
class HomeClassView(View):
    def get(self, request):
        return render(request, 'school/home.html')

# write context in function based view
def aboutfun(request):
    context = {'msg':'Welcome to Function based about view'}
    return render(request, 'school/home.html', context)

# write context in class based view 
class AboutClassView(View):
    def get(self, request):
        context = {'msg':'Welcome to Class Based about view'}
        return render(request, 'school/home.html', context)

## with form in case of function based view 
def contactfun(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank You Form Submitted !!')
    else:
        form = ContactForm()
    return render(request, 'school/contact.html', {'form':form})    

## with form in case of class based view
class ContactClassView(View):

    def get(self, request):
        form = ContactForm()
        return render(request, 'school/contact.html', {'form': form})
    
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank You Form Submitted !!')

## function based views for  
def newsfun(request):
    context = {'info':'Ronaldo is the GOAT.'}
    return render(request, 'school/news.html', context)

""""
second way of doing this this 
views.py
def newsfun(request, template_name):
    template_name = template_name
    context = {'info':'RONALDO is the GOAT'}
    return render(request, template_name, context)

urls.py
path('newsfun/', views.newsfun, {'template_name':'school/news.html'}, name='newsfun')
"""

# news class based view
class NewsClassView(View):
    template_name = ''
    def get(self, request):
        context = {'info': 'Ronaldo is the GOAT'}
        return render(request, self.template_name , context)
    


