from django.db import models

# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.FloatField(max_length=10)
    pages = models.CharField(max_length=10)

