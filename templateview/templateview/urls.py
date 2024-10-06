from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TemplateView.as_view(template_name='school/home.html'), name='home'),
    path('index/', views.TemplateView.as_view(template_name='school/home.html'), name='index'),
    path('home/', views.HomeTemplateView.as_view(), name='home'),
    path('home2/', views.HomeTemplateViewTwo.as_view(), name='home2'),
    path('home3/', views.HomeTemplateViewTwo.as_view(extra_context={'course':'Python'}), name='home3'),
    path('home4/<int:cl>', views.HomeTemplateViewTwo.as_view(), name='about'),
]
