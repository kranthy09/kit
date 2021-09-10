from rest_framework.views import APIView
from django.contrib.auth.models import User
from essentails import serializers
from essentails.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


class UserList(APIView):

    def get(self, request, format=None):
        users = User.objects.all()
        print(users)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)