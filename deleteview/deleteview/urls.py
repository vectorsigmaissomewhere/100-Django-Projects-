from django.contrib import admin
from django.urls import path
from school import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.StudentCreateView.as_view(), name='stucreate'),
    path('thanks/', views.ThanksTemplateView.as_view(), name='thankyou'),
    path('update/<int:pk>', views.StudentUpdateView.as_view(), name='stuupdate'),
    path('thanksupdate/', views.ThanksUpdateView.as_view(), name='thanksupdate'),
    path('create2/', views.StudentCreateView2.as_view(), name='stucreate2'),
    path('update2/<int:pk>', views.StudentUpdateView2.as_view(), name='stuupdate2'),
    path('delete/<int:pk>', views.StudentDeleteView.as_view(), name='studelete'),
    path('delete2/<int:pk>', views.StudentCustomDeleteView.as_view(), name='cusstudelete'),
]
