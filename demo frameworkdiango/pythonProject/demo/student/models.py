from django.db import models

# Create your models here.
class student(models.Model):
    last_name = models.CharField(max_length=50)
    first_name= models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)