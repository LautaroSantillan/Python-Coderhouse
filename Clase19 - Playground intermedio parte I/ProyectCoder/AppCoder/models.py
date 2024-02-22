from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()
    age = models.IntegerField()
    
class Course(models.Model):
    name = models.CharField(max_length=30)
    comision = models.IntegerField()
    
class Teacher(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=60)
    email = models.EmailField()
    profession = models.CharField(max_length=40)
    
class Deliverable(models.Model):
    name = models.CharField(max_length=30)
    deadline = models.DateField()
    delivered = models.BooleanField()