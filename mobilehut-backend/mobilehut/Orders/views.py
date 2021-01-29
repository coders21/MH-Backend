from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import OrderSerializer,OrderUpdateSerializer,ProductOrderSerializer
from .models import Order,ProductOrder
from Products.models import Product,ModelType
from authapp.models import User
#from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

# Order Views

class CreateOrder(APIView):

    def post(self,request):
        payload=request.data
        serializer = OrderSerializer(data=payload)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetOrder(APIView):

    def post(self,request):
        payload=request.data
        try:
            od = Order.objects.filter(order_status=payload['order_status']).values()
        except (KeyError, Order.DoesNotExist):
            return Response('Order Not Found', status.HTTP_404_NOT_FOUND)
        else:
            return Response(od, status=status.HTTP_200_OK)



class ManageOrder(APIView):

    def get(self, request, id):

        try:
            od = Order.objects.get(id=int(id))
        except (KeyError, Order.DoesNotExist):
            return Response('Order Not Found', status.HTTP_404_NOT_FOUND)
        else:
            serializer = OrderSerializer(od)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):

        try:
            od = Order.objects.get(id=int(id))
        except (KeyError, Order.DoesNotExist):
            return Response('Order Not Found', status.HTTP_404_NOT_FOUND)
        else:
            payload = request.data
            serializer = OrderUpdateSerializer(od,data=payload)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# Create Product Order

class CreateProductOrder(APIView):

    def get(self,request):
        return Response([ProductOrderSerializer(od).data for od in ProductOrder.objects.all()])

    def post(self,request):
        payload=request.data
        serializer = ProductOrderSerializer(data=payload)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ManageProductOrder(APIView):

    def get(self, request, id):

        try:
            od = ProductOrder.objects.get(id=int(id))
        except (KeyError, ProductOrder.DoesNotExist):
            return Response('Product Order Not Found', status.HTTP_404_NOT_FOUND)
        else:
            serializer = ProductOrderSerializer(od)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):

        try:
            od = ProductOrder.objects.get(id=int(id))
        except (KeyError, ProductOrder.DoesNotExist):
            return Response('Product Order Not Found', status.HTTP_404_NOT_FOUND)
        else:
            payload = request.data
            serializer = ProductOrderSerializer(od,data=payload)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class GetPOrder(APIView):

    def get(self,request,id):
        order_details=[]
        product_details=[]
        order_info=list(Order.objects.filter(id=id).values())
        porders=ProductOrder.objects.filter(order=id).values()
        user=User.objects.get(id=order_info[0]['user_id'])
      
        for x in range(0,len(porders)):
            prod=list(Product.objects.filter(id=porders[x]['product_id']).values())
            model=ModelType.objects.get(id=prod[0]['product_model_id'])
            prod[0]['model_name']=model.model_name
            product_details.append(prod[0])
        
        order_info[0]['products']=product_details
        order_info[0]['customername']=user.username
        order_info[0]['customercity']=user.city
        order_info[0]['customerprovince']=user.province
        order_info[0]['customeraddress']=user.address
        order_info[0]['customerphonenumber']=user.phonenumber
        return Response(order_info,status=status.HTTP_200_OK)