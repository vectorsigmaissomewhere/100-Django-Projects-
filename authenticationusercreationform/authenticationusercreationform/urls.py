from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.sign_up,name='signup'), # the third url means when other url wants to open the signup it need signup
    path('login/',views.user_login,name='login'),
    path('profile/',views.user_profile, name='profile'),
    path('logout/',views.user_logout, name='logout'),
    path('changepass/', views.user_change_pass, name='changepass'), # link to change password with old password
    path('changepass1/', views.user_change_pass1, name='changepass1') # link to change password without old password
]
