from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
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