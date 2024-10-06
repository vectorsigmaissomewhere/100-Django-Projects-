from django.db import models

# gettting name data by order
class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('name')