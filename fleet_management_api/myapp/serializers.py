from rest_framework import serializers
from .models import Taxi, Trajectory

class TaxiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxi
        fields = '__all__'

class TrajectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Trajectory
        fields = '__all__'