from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Trip(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    duration = models.TimeField()
    max_size = models.IntegerField()
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    date_entered = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name

class Theme(models.Model):
    name = models.CharField(max_length=200)
    trip = models.ForeignKey('Trip')
    
    def __str__(self):
        return self.name
