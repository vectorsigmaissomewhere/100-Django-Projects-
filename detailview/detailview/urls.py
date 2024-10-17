from django.contrib import admin
from django.urls import path
from school import views 

urlpatterns = [
    path('admin/', admin.site.urls), 
    # why use need to pass pk is because it is detailview 
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name='studentdetail'),
    path('customstudent/<int:pk>/', views.StudentDetailCustomTemplateView.as_view(), name='customdetail'),
    path('customcontextstudent/<int:pk>/', views.StudentDetailCustomContextView.as_view(), name='customcontext'),
    path('studentlistview/', views.StudentListView.as_view(), name='studentlistview'),
]
