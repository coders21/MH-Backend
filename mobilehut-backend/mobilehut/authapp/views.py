from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer,UserUpdateSerializer,CustomTokenObtainPairSerializer
from .models import User
from Orders.models import Order,ProductOrder
from rest_framework import status
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
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
        
        user_address=[]
        user_address.append({"phonenumber":user.phonenumber,"address":user.address,"city":user.city,"province":user.province})
        
        user_account=[]
        user_account.append({"name":user.username,"email":user.email})

        account_details={}
        account_details['order']=order_details
        account_details['address']=user_address
        account_details['account']=user_account

        return Response(account_details,status=status.HTTP_200_OK)