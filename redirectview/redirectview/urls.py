from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TemplateView.as_view(template_name='school/home.html'), name='blankhome'),
    # when I hit home url it should get rediect to / url 
    path('home/', views.RedirectView.as_view(url='/'), name='home'), 
    # when I hit the pattern url it should get redirect to home pattern_name should be same as name 
    path('pattern/', views.RedirectView.as_view(pattern_name='home'), name='pattern'),
    # if some one goes to ronaldo url it will get redirected to google.com
    path('ronaldo/', views.RedirectView.as_view(url='https://www.google.com'), name='ronaldo'),
    # this is related to views.py
    path('ronaldosecond/', views.RonaldoRedirectView.as_view(), name='ronaldosecond'),
    
    #  working with MbappeRedirectView, when i hit mbappe/11 what happens
    path('mbappe/<int:pk>', views.MbappeRedirectView.as_view(),name='mbappe'),
    # when I hit mbappe/number it takes me to home but it doesn't hit the ''/number url but ''
    path('<int:pk>/', views.TemplateView.as_view(template_name='school/home.html'), name='mindex'),


    # sending string instead of number 
    path('balatoli/<slug:post>/', views.MbappeRedirectView.as_view(), name='balatoli'),
    path('<slug:post>/', views.TemplateView.as_view(template_name='school/home.html'), name='mindex'),
]
