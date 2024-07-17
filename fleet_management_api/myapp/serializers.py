from rest_framework import serializers
from .models import Taxi, Trajectory
from django.contrib.auth.models import User

class TaxiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxi
        fields = '__all__'

class TrajectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Trajectory
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_active', 'is_staff', 'date_joined') 