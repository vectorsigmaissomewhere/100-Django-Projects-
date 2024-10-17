from django.urls import path, include 
from registration import views 

urlpatterns = [
    path('profile/', views.ProfileTemplateView.as_view(), name='profile')
]