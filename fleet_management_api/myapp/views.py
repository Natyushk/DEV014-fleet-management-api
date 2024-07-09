from contextvars import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Taxi  
from .serializers import TaxiSerializer
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth import authenticate


class TaxisView(APIView):
    pagination_class = PageNumberPagination
    
    def get(self, request):
        plate_filter = request.query_params.get('plate', None)  # Get optional license plate filter
        taxis = Taxi.objects.filter(plate__contains=plate_filter) if plate_filter else Taxi.objects.all()
        serializer = TaxiSerializer(taxis, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TrajectoriesView(APIView):
    pagination_class = PageNumberPagination
    
    def get(self, request):
        taxi_id = request.query_params.get('taxi_id', None) 
        date = request.query_params.get('date', None) 
        
class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password:
            return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)
        
        if user.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = user.objects.create_user(username=username, password=password)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
             # User is authenticated
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            # Invalid credentials
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)        
        