from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('',include('personalblog.urls')),
    path('', include('integrateapiwithhtmlcssandjs.urls')),
    path('admin/', admin.site.urls),
]

