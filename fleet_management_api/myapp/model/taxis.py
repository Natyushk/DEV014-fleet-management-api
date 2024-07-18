from django.db import models

class Taxi(models.Model):
    plate = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.plate