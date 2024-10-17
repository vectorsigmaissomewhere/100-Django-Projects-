from django.contrib import admin
from django.urls import path, include 
from registration import views
from django.contrib.auth.decorators import login_required
# from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    path('about/', login_required(views.AboutTemplateView.as_view()), name='about'),
    # path('about/', staff_member_required(views.AboutTemplateView.as_view()), name='about'),
    # login_required in views
    path('classabout/', views.AboutClassTemplateView.as_view(), name='classabout'),
    # item 3 
    path('classdecabout/', views.AboutClassDecTemplateView.as_view(), name='classdecabout'),
]
