from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer,UserUpdateSerializer,CustomTokenObtainPairSerializer,ChangePasswordSerializer
from .models import User
from Orders.models import Order,ProductOrder
from django.contrib.auth import authenticate,login
from rest_framework import status
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)


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

    def get(self, request,id):

       
        try:
            user = User.objects.get(id=id)
        except (KeyError, User.DoesNotExist):
            return Response('User Not Found', status.HTTP_404_NOT_FOUND)
        else:
            serializer = UserUpdateSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request,id):

        
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


class CustomTokenObtainPairView(TokenObtainPairView):  # to add token and 
    # Replace the serializer with your custom
    serializer_class = CustomTokenObtainPairSerializer


class AccountDetail(APIView):

    def post(self,request):

        email=request.data.get('email')
        user=User.objects.get(email=email)
        order=Order.objects.filter(user=user).prefetch_related('productorder_set')
        order_details=[]  # order details
        product_details=[]
      

        index=0
        for order in order:
            order_details.append({"ordernumber":order.id,"orderdate":order.order_date,"orderstatus":order.order_status,"ordertracking":order.order_tracking,"updateddate":order.update_date})
            for order in order.productorder_set.all():
                product_details.append({"name":order.product.product_name,"quantity":order.quantity,"model":order.modelP,"colour":order.colour})
            order_details[index]['product']=product_details
            product_details=[]
            index=index+1
        

        account_details={}
        account_details['order']=order_details
        account_details['address']={"phonenumber":user.phonenumber,"address":user.address,"city":user.city,"province":user.province}
        account_details['account']={"name":user.username,"email":user.email,"id":user.id}

        return Response(account_details,status=status.HTTP_200_OK)


class UpdatePassword(APIView):


    def get_object(self,request, email,password):
        my_user=User.objects.get(email=email)
        user = User.objects.get(email=my_user.email)
        login(request,user,backend='django.contrib.auth.backends.ModelBackend')
        return self.request.user

    def put(self, request, *args, **kwargs):
        email=request.data.get('email')
        password=request.data.get('old_password')
        self.object = self.get_object(request,email,password)
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            old_password = serializer.data.get("old_password")
            if not self.object.check_password(old_password):
                return Response({"old_password": ["Wrong password."]},
                                status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateSocial(APIView):

    def post(self,request):

        email=request.data.get('email')
        
        user=User.objects.filter(email=email).values()

        if len(user)>0: # if user is already there retrieve id
            user_serializer={
                "id":user[0]['id'],
                "email":user[0]['email'],
                }
        else:
            user=User.objects.create(email=email)
            user.save()
            user_serializer={
                    "id":user.id,
                    "email":user.email,
            }

             
        
        return Response(user_serializer,status=status.HTTP_200_OK)
          


