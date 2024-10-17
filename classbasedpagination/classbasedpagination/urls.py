from django.contrib import admin
from django.urls import path
from blog import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.PostListView.as_view(), name='home'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post'),
]
