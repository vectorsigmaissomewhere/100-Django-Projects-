from django.contrib import admin
from django.urls import path, include
from registration import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    path('about/', views.about, name='about')
]
