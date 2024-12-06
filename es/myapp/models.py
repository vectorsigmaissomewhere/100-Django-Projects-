from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    summary = models.TextField()

    def __str__(self):
        return self.title
