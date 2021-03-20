from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User

class UserSerializer(ModelSerializer):

  class Meta:

        model = User
        fields = ['id','email','password', 'username','phonenumber','address','city',
                  'province']

  def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.save()
        return user

  def update(self, instance, validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)
            instance.save()
        return instance

class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','username','phonenumber','address','city',
                  'province']

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.save()
        return user

    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)
            instance.save()
        return instance


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer): # to add username and id with tokens
    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        # Custom data you want to include
        if (self.user.is_superuser):
            data.update({'email': self.user.email})
            data.update({'userid': self.user.id})
        else:
            data.update({'email': self.user.email})
            data.update({'userid': self.user.id})
            del data['refresh']
            del data['access']
        # and everything else you want to send in the response
        return data



class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


    def validate_new_password(self, value):
        validate_password(value)
        return value