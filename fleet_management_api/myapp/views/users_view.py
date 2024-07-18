from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth import authenticate
from ..serializers import UserSerializer
from django.contrib.auth.models import User

class UsersView(APIView):
    pagination_class = PageNumberPagination

    def get(self, request):
        # Get all users
        users = User.objects.all()

        # Page the results pagination 
        if self.pagination_class:
            paginator = self.pagination_class()
            paginated_users = paginator.paginate(users)
            serializer = UserSerializer(paginated_users, many=True)
            return paginator.get_paginated_response(serializer.data)

        # Serialize all users otherwise
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)