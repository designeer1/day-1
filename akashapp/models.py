from django.db import models
class student(models.Model):
    n=models.CharField(max_length=255)
    r=models.TextField()
# Create your models here.
