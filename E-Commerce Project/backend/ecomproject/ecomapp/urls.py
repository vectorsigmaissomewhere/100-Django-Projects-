from ecomapp import views
from django.urls import path, include

urlpatterns = [
    path('',views.getRoutes, name="getRoutes"),
]