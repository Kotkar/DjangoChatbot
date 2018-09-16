from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from authentication.serializers import UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserCreate(CreateAPIView):
    """ 
    Creates the user. 
    """
    serializer_class = UserSerializer

class UserLogin(UserCreate):
    """
    Authenticate existing user.
    """
    serializer_class = UserSerializer

    def post(self, request, format='json'):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if not user:
            return Response({"error": "Login failed"}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = self.get_serializer(user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)
