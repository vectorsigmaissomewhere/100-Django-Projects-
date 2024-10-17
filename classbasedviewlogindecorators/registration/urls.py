from django.urls import path, include 
from registration import views 
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # item 1
    path('profile/', login_required(views.ProfileTemplateView.as_view()), name='profile'),
    # item 2
    path('classprofile/', views.ProfileClassTemplateView.as_view(), name='classprofile'),
    # item 3 
    path('classdecprofile/', views.ProfileClassDecTemplateView.as_view(), name='classdecprofile'),
]