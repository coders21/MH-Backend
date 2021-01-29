from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer,UserUpdateSerializer
from .models import User
from rest_framework import status

# Create your views here.

class CreateUser(APIView):

    def get(self, request):
        return Response([UserSerializer(user).data for user in User.objects.all()])

    def post(self, request):
        payload = request.data
        serializer = UserSerializer(data=payload)

        if serializer.is_valid():
            instance = serializer.save()
            instance.set_password(instance.password)
            instance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ManageUser(APIView):

    def get(self, request, id):

        try:
            user = User.objects.get(id=id)
        except (KeyError, User.DoesNotExist):
            return Response('User Not Found', status.HTTP_404_NOT_FOUND)
        else:
            serializer = UserUpdateSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):

        try:
            user = User.objects.get(id=id)
        except (KeyError, User.DoesNotExist):
            return Response('User Not Found', status.HTTP_404_NOT_FOUND)
        else:
            payload = request.data
            serializer = UserUpdateSerializer(user,data=payload)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):

        try:
            user = User.objects.get(id=id)
        except (KeyError, User.DoesNotExist):
            return Response('User Not Found', status.HTTP_404_NOT_FOUND)
        else:
            user.delete()