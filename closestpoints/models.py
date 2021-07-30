from django.db import models


# Create your models here.
class Points(models.Model):
    input = models.TextField()
    output = models.TextField()
