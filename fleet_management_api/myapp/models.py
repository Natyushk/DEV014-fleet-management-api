from django.db import models

# Create your models here.
class Taxi(models.Model):
    plate = models.CharField(max_length=20, unique=True)

class Trajectory(models.Model):
    taxi = models.ForeignKey(Taxi, on_delete=models.CASCADE)
    date = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()