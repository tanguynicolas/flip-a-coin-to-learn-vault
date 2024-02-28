from django.db import models

# Create your models here.

class Score(models.Model):
    heads = models.IntegerField(default=0)
    tails = models.IntegerField(default=0)
