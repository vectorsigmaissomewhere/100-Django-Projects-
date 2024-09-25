from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('firstmethod/', views.firstmethod),
    path('lastmethod/', views.lastmethod),
    path('latestmethod/', views.latestmethod),
    path('earliestmethod/', views.earliestmethod),
    path('existmethod/', views.existmethod),
    path('createmethod/', views.createmethod),
    path('getorcreated/', views.get_or_create),
    path('update/', views.update),
    path('updateorcreate/', views.update_or_create), # this is not working 
    path('bulkcreate/', views.bulk_create),
    path('bulkupdate/', views.bulk_update),
    path('inbulk/', views.in_bulk),
    path('deletemethod/', views.deletemethod),
    path('countmethod/', views.countmethod),
    path('explainmethod/', views.explainmethod),
]
