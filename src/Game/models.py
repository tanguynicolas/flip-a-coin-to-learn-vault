from django.db import models

# Create your models here.

class Result(models.Model):
    heads = models.IntegerField(default=0)
    tails = models.IntegerField(default=0)
