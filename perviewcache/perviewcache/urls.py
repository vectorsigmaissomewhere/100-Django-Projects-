from django.contrib import admin
from django.urls import path
from enroll import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.home),
    path('',cache_page(120)(views.home)),
    path('home/',views.home),
    path('contact/', views.contact),
]
