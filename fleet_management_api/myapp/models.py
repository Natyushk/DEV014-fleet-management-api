from django.db import models


# Create your models here.
class Taxi(models.Model):
    plate = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.plate

class Trajectory(models.Model):
    taxi = models.ForeignKey(Taxi, on_delete=models.CASCADE)
    date = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    def __str__(self):
        return f"{self.taxi.plate} - {self.date}"
