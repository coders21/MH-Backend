from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import OrderSerializer,OrderUpdateSerializer,ProductOrderSerializer,CoupanSerializer
from .models import Order,ProductOrder,Coupan
from Products.models import Product,ModelType,ProductModel
from authapp.models import User
from rest_framework.permissions import IsAuthenticated
#from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly,BasePermission, SAFE_METHODS
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
        permission_classes=[IsAuthenticatedOrReadOnly]
        try:
            od = list(Order.objects.filter(order_status=payload['order_status']).values())
            nonuser=od
           
            for x in range(0,len(od)):
                try:
                    user=User.objects.get(id=od[x]['user_id'])
                    od[x]['customername']=user.username
                    od[x]['customercity']=user.city
                    od[x]['customerprovince']=user.province
                    od[x]['customeraddress']=user.address+','+user.city+','+user.province
                    od[x]['customerphonenumber']=user.phonenumber
                    od[x]['customeremail']=user.email
                except:
                    od[x]['customername']=nonuser[x]['customername']
                    od[x]['customercity']=nonuser[x]['customercity']
                    od[x]['customerprovince']=nonuser[x]['customerprovince']
                    od[x]['customeraddress']=nonuser[x]['customeraddress']+','+nonuser[x]['customercity']+','+nonuser[x]['customerprovince']
                    od[x]['customerphonenumber']=nonuser[x]['customerphonenumber']

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
        name=payload['product'].replace('-',' ')
        product=Product.objects.get(product_name=name)
        payload['product']=product.id
       
        serializer = ProductOrderSerializer(data=payload)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ManageProductOrder(APIView):

    permission_classes=[IsAuthenticatedOrReadOnly]

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

    permission_classes=[IsAuthenticatedOrReadOnly]

    def get(self,request,id):
        order_details=[]
        product_details=[]
        #order_info=list(Order.objects.filter(id=id).values())
        porders=ProductOrder.objects.filter(order=id).values()
       
      
        for x in range(0,len(porders)):
            prod=list(Product.objects.filter(id=porders[x]['product_id']).values())
          
            prod[0]['quantity']=porders[x]['quantity']
            prod[0]['colour']=porders[x]['colour']
            modelname=ModelType.objects.get(id=porders[x]['modelP'])
            prod[0]['model_name']=modelname.model_name
            product_details.append(prod[0])
        
        my_dict={'products':None}
        my_dict['products']=product_details
        #order_info[0]['products']=product_details
        return Response(my_dict,status=status.HTTP_200_OK)


class CreateCoupan(APIView):

    def get(self,request):
        return Response([CoupanSerializer(od).data for od in Coupan.objects.all()])

    def post(self,request):
        payload=request.data
        serializer = CoupanSerializer(data=payload)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ManageCoupan(APIView):

    def get(self, request, id):

        try:
            cp = Coupan.objects.get(id=int(id))
        except (KeyError, Coupan.DoesNotExist):
            return Response('Coupan Not Found', status.HTTP_404_NOT_FOUND)
        else:
            serializer = CoupanSerializer(cp)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):

        try:
            cp = Coupan.objects.get(id=int(id))
        except (KeyError, Coupan.DoesNotExist):
            return Response('Coupan Not Found', status.HTTP_404_NOT_FOUND)
        else:
            payload = request.data
            serializer = CoupanSerializer(cp,data=payload)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):

        try:
            cp = Coupan.objects.get(id=int(id))
        except (KeyError, Coupan.DoesNotExist):
            return Response('Coupan Not Found', status.HTTP_404_NOT_FOUND)
        else:
            cp.delete()
            return Response("Coupan Deleted", status.HTTP_200_OK)


SAFE_METHODS = ['POST','PUT','DELETE']
class IsAuthenticatedOrReadOnly(BasePermission):
    """
    The request is authenticated as a user.
    """

    def has_permission(self, request, view):
        if (request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated()):
            return True
        return False