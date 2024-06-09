from django.db import models

class Dentist(models.Model):
    tuition = models.IntegerField()
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return f"Dentist {self.name}. Tuition {self.tuition}"
    
    
