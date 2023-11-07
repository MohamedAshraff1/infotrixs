from django.db import models

# Create your models here.


class random(models.Model):

    quotes = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=50, null=True)
