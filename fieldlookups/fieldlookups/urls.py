from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('exact', views.exact),
    path('iexact', views.iexact),
    path('contains', views.contains),
    path('icontains', views.icontains),
    path('inlookup', views.inlookup),
    path('greaterthan', views.greaterthan),
    path('greaterthanequal', views.greaterthanequal),
    path('lessthan', views.lessthan),
    path('lessthanequal', views.lessthanequal),
    path('startswith', views.startswith),
    path('istartswith', views.istartswith),
    path('endswith', views.endswith),
    path('iendswith', views.iendswith),
    path('range', views.range),
    path('datelookup', views.datelookup),
]
