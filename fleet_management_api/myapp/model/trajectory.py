from django.db import models
from .taxis import Taxi

class Trajectory(models.Model):
    taxi = models.ForeignKey(Taxi, on_delete=models.CASCADE)
    date = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    def __str__(self):
        return f"{self.taxi.plate} - {self.date}"