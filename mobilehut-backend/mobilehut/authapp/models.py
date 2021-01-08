from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self,email,password):
        user=self.model(email=email)
        user.password=password
        user.set_password(user.password)
        user.save()

    def create_staffuser(self,email,password):
        user = self.model(email=email)
        user.password=password
        user.set_password(user.password)
        # user.is_admin = True
        user.is_superuser = False
        user.is_staff = True
        user.is_active = True
        user.save()

    def create_superuser(self,email,password):
        user=self.model(email=email)
        #user.password=password
        user.set_password(password)
        user.is_staff=True
        user.is_superuser=True
        user.save()

    def get_by_natural_key(self, email_):
        return self.get(email=email_)

    

class User(AbstractBaseUser,PermissionsMixin):

    # is_admin=models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    city=models.CharField(max_length=20,blank=True)
    province=models.CharField(max_length=30,blank=True)
    address=models.CharField(max_length=200,blank=True)
    date_joined = models.DateTimeField(null=True, blank=True)
    username = models.CharField(

        max_length=150,
        unique=True,
        null=True,

    )
    is_active = models.BooleanField(default=True)
    address=models.CharField(max_length=150,null=True,blank=True)
    object = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_short_name(self):
        return self.email