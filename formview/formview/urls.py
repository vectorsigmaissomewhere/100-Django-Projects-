from django.contrib import admin
from django.urls import path
from school import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('thankyou/', views.ThanksTemplateView.as_view(), name='thankyou'),
]
