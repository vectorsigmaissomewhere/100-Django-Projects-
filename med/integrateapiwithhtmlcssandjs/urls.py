from django.urls import path
from .views import ItemListCreate, index

urlpatterns = [
    path('', index, name='index'),
    path('api/items/', ItemListCreate.as_view(), name='item-list-create'),
]
