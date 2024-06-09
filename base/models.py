from django.db import models

class Dentist(models.Model):
    tuition = models.IntegerField()
    name = models.CharField(max_length=20)
    
class Patient(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    
