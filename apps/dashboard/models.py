from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Asset(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    model_number = models.CharField(max_length=100,null=True,blank=True)
    availability =models.BooleanField(default=True)
    added_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.ForeignKey('Designation',on_delete=models.CASCADE)
    phone =models.IntegerField()
    address = models.CharField(max_length=100)
    status =models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Designation(models.Model):
    name = models.CharField(max_length=100)
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name