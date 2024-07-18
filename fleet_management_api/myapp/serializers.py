from rest_framework import serializers
from .model.taxis import Taxi
from .model.trajectory import Trajectory
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
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name') 
        
    def create(self, validated_data):
        """
        Create and save a new user with the given validated data.
        """
        password = validated_data.pop('password')
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],  # Add extra fields as needed
            last_name=validated_data['last_name'],  # Add extra fields as needed
        )
        user.set_password(password)
        user.save()
        return user