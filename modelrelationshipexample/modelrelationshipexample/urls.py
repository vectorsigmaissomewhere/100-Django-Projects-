from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('user/', views.show_user_data, name='user'),
    path('page/', views.show_page_data, name='page'),
    path('post/', views.show_post_data, name='post'),
    path('song/', views.show_song_data, name='song'),
]
