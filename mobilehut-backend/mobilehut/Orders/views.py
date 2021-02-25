from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import OrderSerializer,OrderUpdateSerializer,ProductOrderSerializer
from .models import Order,ProductOrder
from Products.models import Product,ModelType
from authapp.models import User
from rest_framework.permissions import IsAuthenticated
#from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

# Order Views

class CreateOrder(APIView):

    permission_classes = [IsAuthenticated]

    def post(self,request):
        payload=request.data
        serializer = OrderSerializer(data=payload)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetOrder(APIView):

    permission_classes = [IsAuthenticated]

    def post(self,request):
        payload=request.data
        try:
            od = list(Order.objects.filter(order_status=payload['order_status']).values())
        
            for x in range(0,len(od)):
                user=User.objects.get(id=od[x]['user_id'])
                od[x]['customername']=user.username
                od[x]['customercity']=user.city
                od[x]['customerprovince']=user.province
                od[x]['customeraddress']=user.address
                od[x]['customerphonenumber']=user.phonenumber
           
        except (KeyError, Order.DoesNotExist):
            return Response('Order Not Found', status.HTTP_404_NOT_FOUND)
        else:
            return Response(od, status=status.HTTP_200_OK)



class ManageOrder(APIView):

    permission_classes = [IsAuthenticated]

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

    permission_classes = [IsAuthenticated]

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

    permission_classes = [IsAuthenticated]

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

    permission_classes = [IsAuthenticated]

    def get(self,request,id):
        order_details=[]
        product_details=[]
        #order_info=list(Order.objects.filter(id=id).values())
        porders=ProductOrder.objects.filter(order=id).values()
        
      
        for x in range(0,len(porders)):
            prod=list(Product.objects.filter(id=porders[x]['product_id']).values())
            prod[0]['quantity']=porders[x]['quantity']
            prod[0]['colour']=porders[x]['colour']
            prod[0]['model_name']=porders[x]['modelP']
            product_details.append(prod[0])
        
        my_dict={'products':None}
        my_dict['products']=product_details
        #order_info[0]['products']=product_details
        return Response(my_dict,status=status.HTTP_200_OK)