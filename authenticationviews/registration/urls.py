from django.urls import path 
from registration import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
]