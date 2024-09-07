signals.py
```python
from django.dispatch import Signal, receiver
# Creating Signals
notification = Signal(providing_args=["request", "user"])

# Reciver Function
@receiver(notification)
def show_notification(sender, **kwargs):
    print(sender)
    print(f'{kwargs}')
    print("Notification")
```

views.py
```python
from django.shortcuts import render, HttpResponse
from blog import signals

def home(request):
    signals.notification.send(sender=None, request=request, user=['Albert', 'Einstein'])
    return HttpResponse("This is Home Page")
```

urls.py
```python
from django.contrib import admin
from django.urls import path
from blog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
]
```