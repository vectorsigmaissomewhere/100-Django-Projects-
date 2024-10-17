from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # this url shows listview
    path('student/', views.StudentListView.as_view(), name='student'),
    path('studentsecond/', views.StudentSecondListView.as_view(), name='studentsecond'),
    path('studentthird/', views.StudentThirdListView.as_view(), name='studentthird'),
    path('studentfourth/', views.StudentFourthListView.as_view(), name='studentfourth'),
    path('studentfifth/', views.StudentFifthListView.as_view(), name='studentfifth'),
]
