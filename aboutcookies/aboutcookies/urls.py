from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('set/', views.setcookie),
    path('get/',views.getcookie),
    path('del/', views.delcookie),
]
