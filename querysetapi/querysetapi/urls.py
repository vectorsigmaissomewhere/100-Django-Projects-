from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.queryall),
    path('queryfilter/', views.queryfilter),
    path('queryexclude/', views.queryexclude),
    path('queryorderby/', views.queryascendingorderby),
    path('queryorderbyneg/', views.querydescendingorderby),
    path('queryrandom/', views.queryrandom),
    path('queryreverse/', views.queryreverse),
    path('queryvalues/', views.queryvalues),
    path('queryvalueslist/', views.queryvalueslist),
    path('usingmethod/', views.using),
    path('querydates/', views.querydates),
    path('queryunion/', views.queryunion),
    path('queryintersection/', views.queryintersection),
    path('querydifference/', views.querydifference),
    path('andoperator/', views.andoperator),
    path('oroperator/', views.oroperator),
]
