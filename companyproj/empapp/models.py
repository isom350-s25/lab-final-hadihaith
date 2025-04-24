from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    extension = models.CharField(max_length=10)
    email = models.EmailField()
    title = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    DOB = models.DateField(null=True, blank=True, default="2000-01-01")
    hire_date = models.DateField(null=True, blank=True, default="2025-01-01")
