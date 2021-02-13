from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ProductSerializer,CategorySerializer,BrandSerializer,ModelSerializer,ColourSerializer,ProductImgSerializer
from .models import Product,Category,Brand,ModelType,Colour,ProductImages
from rest_framework.permissions import IsAuthenticated
from Orders.models import Order
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
#from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
#### CATEGORY VIEWS ####


class CreateCategory(APIView):

    #permission_classes = [IsAuthenticated]
   

    def get(self,request):
        return Response([CategorySerializer(cat).data for cat in Category.objects.all()])

    def post(self,request):
        payload=request.data
        serializer = CategorySerializer(data=payload)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ManageCategory(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, id):

        try:
            cat = Category.objects.get(id=int(id))
        except (KeyError, Category.DoesNotExist):
            return Response('Category Not Found', status.HTTP_404_NOT_FOUND)
        else:
            serializer = CategorySerializer(cat)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):

        try:
            cat = Category.objects.get(id=int(id))
        except (KeyError, Category.DoesNotExist):
            return Response('Category Not Found', status.HTTP_404_NOT_FOUND)
        else:
            payload = request.data
            serializer = CategorySerializer(cat,data=payload)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):

        try:
            cat = Category.objects.get(id=int(id))
        except (KeyError, Category.DoesNotExist):
            return Response('Category Not Found', status.HTTP_404_NOT_FOUND)
        else:
            cat.delete()

            return Response("Category Deleted",status=status.HTTP_200_OK)

###  BRAND VIEWS ####

class CreateBrand(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request):
        return Response([BrandSerializer(dat).data for dat in Brand.objects.all()])

    def post(self,request):
        payload=request.data
        serializer = BrandSerializer(data=payload)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ManageBrand(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, id):

        try:
            brnd = Brand.objects.get(id=int(id))
        except (KeyError, Brand.DoesNotExist):
            return Response('Brand Not Found', status.HTTP_404_NOT_FOUND)
        else:
            serializer = BrandSerializer(brnd)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):

        try:
            brnd = Brand.objects.get(id=int(id))
        except (KeyError, Brand.DoesNotExist):
            return Response('Brand Not Found', status.HTTP_404_NOT_FOUND)
        else:
            payload = request.data
            serializer = BrandSerializer(brnd,data=payload)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):

        try:
            brnd = Brand.objects.get(id=int(id))
        except (KeyError, Brand.DoesNotExist):
            return Response('Brand Not Found', status.HTTP_404_NOT_FOUND)
        else:
            brnd.delete()

            return Response("Brand Deleted",status=status.HTTP_200_OK)

#### MODEL VIEWS ####

class CreateModel(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request):
        return Response([ModelSerializer(dat).data for dat in ModelType.objects.all()])

    def post(self,request):
        payload=request.data
        serializer = ModelSerializer(data=payload)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ManageModel(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, id):

        try:
            model = ModelType.objects.get(id=int(id))
        except (KeyError, ModelType.DoesNotExist):
            return Response('Model Not Found', status.HTTP_404_NOT_FOUND)
        else:
            serializer = ModelSerializer(model)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):

        try:
            model = ModelType.objects.get(id=int(id))
        except (KeyError, ModelType.DoesNotExist):
            return Response('Model Not Found', status.HTTP_404_NOT_FOUND)
        else:
            payload = request.data
            serializer = ModelSerializer(model,data=payload)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):

        try:
            model = ModelType.objects.get(id=int(id))
        except (KeyError, ModelType.DoesNotExist):
            return Response('Model Not Found', status.HTTP_404_NOT_FOUND)
        else:
            model.delete()

            return Response("Model Deleted",status=status.HTTP_200_OK)

#### PRODUCT VIEWS ####
class CreateProduct(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request):
        return Response([ProductSerializer(dat).data for dat in Product.objects.all()])

    def post(self,request):
        payload=request.data
        #print(payload)
        serializer = ProductSerializer(data=payload)
        #product=Product.objects.create(product_name=payload['product_name'],product_quantity=payload['product_quantity'],product_price=int(payload['product_price']),product_sku=payload['product_sku'],product_description=payload['product_description'],product_model=payload['product_model'],product_category=int(payload['product_category']),product_brand=int(payload['product_brand']))
        #product.save()
        #print(payload)
        #Product.objects.create("product_name")
        
        if serializer.is_valid():
            serializer.save()
            productobj=Product.objects.get(id=serializer.data['id'])
            #now save colour 
            for x in payload['product_colors']:
                Colour.objects.create(colour_name=x['name'],colour_product=productobj)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ManageProduct(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, id):

        try:
            pro = Product.objects.get(id=int(id))
        except (KeyError, Product.DoesNotExist):
            return Response('Product Not Found', status.HTTP_404_NOT_FOUND)
        else:
            serializer = ProductSerializer(pro)
            colour=Colour.objects.filter(colour_product=pro.id).values()
            
            select_colour={}
            append_color=[]
            for x in range(0,len(colour)):
                select_colour['id']=colour[x]['colour_name']
                select_colour['name']=colour[x]['colour_name']
                append_color.append(select_colour)
                select_colour={}
                
            product_data=serializer.data
            product_data['product_colors']=append_color
            
            
            return Response(product_data, status=status.HTTP_200_OK)

    def put(self, request, id):

        try:
            pro = Product.objects.get(id=int(id))
        except (KeyError, Product.DoesNotExist):
            return Response('Product Not Found', status.HTTP_404_NOT_FOUND)
        else:
            payload = request.data
            serializer = ProductSerializer(pro,data=payload)
            
            clr=Colour.objects.filter(colour_product=pro.id).values()
            # first delete all colours of existing product and then add again
            for x in clr:
                del_colour=Colour.objects.get(id=int(x['id']))
                del_colour.delete()
            

            #now save colour 
            for x in payload['product_colors']:
                Colour.objects.create(colour_name=x['name'],colour_product=pro)
            


            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):

        try:
            pro = Product.objects.get(id=int(id))
        except (KeyError, Product.DoesNotExist):
            return Response('Product Not Found', status.HTTP_404_NOT_FOUND)
        else:
            pro.delete()

            return Response("Product Deleted",status=status.HTTP_200_OK)

#### Color VIEWS ####
class CreateColour(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request):
        return Response([ColourSerializer(dat).data for dat in Colour.objects.all()])

    def post(self,request):
        payload=request.data
        serializer = ColourSerializer(data=payload)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ManageColour(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, id):

        try:
            color = Colour.objects.get(id=int(id))
        except (KeyError, Colour.DoesNotExist):
            return Response('Colour Not Found', status.HTTP_404_NOT_FOUND)
        else:
            serializer = ColourSerializer(color)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):

        try:
            color = Colour.objects.get(id=int(id))
        except (KeyError, Colour.DoesNotExist):
            return Response('Colour Not Found', status.HTTP_404_NOT_FOUND)
        else:
            payload = request.data
            serializer = ColourSerializer(color,data=payload)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):

        try:
            color = Colour.objects.get(id=int(id))
        except (KeyError, Colour.DoesNotExist):
            return Response('Colour Not Found', status.HTTP_404_NOT_FOUND)
        else:
            color.delete()

            return Response("Product Deleted",status=status.HTTP_200_OK)

## IMAGE VIEWS ##
class CreateProductImages(APIView):

     #permission_classes = [IsAuthenticated]

     parser_classes = (MultiPartParser, FormParser)

     def get(self,request):
        return Response([ProductImgSerializer(dat).data for dat in ProductImages.objects.all()])

     def post(self,request):
        payload=request.data
        serializer=ProductImgSerializer(data=payload)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

## delete or add more images
class ManageProductImages(APIView):

    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, id):

        try:
            img = ProductImages.objects.filter(image_product=int(id)).values()
        except (KeyError, ProductImages.DoesNotExist):
            return Response('Product Images Not Found', status.HTTP_404_NOT_FOUND)
        else:

            #serializer = ProductImgSerializer(img)
            return Response(img, status=status.HTTP_200_OK)

    
    def delete(self,request,id):

        try:
            delimg = ProductImages.objects.get(id=int(id))
        except (KeyError, ProductImages.DoesNotExist):
            return Response('Image Not Found', status.HTTP_404_NOT_FOUND)
        else:
            delimg.delete()

            return Response("Product Deleted",status=status.HTTP_200_OK)


# Get Total Brands,Models,Categories
class GetTotal(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request):

        total={
            "total_brands":0,
            "total_models":0,
            "total_categories":0,
            "total_products":0,
            "total_orders":0
        }

        total_brands=Brand.objects.all().values()
        total_models=ModelType.objects.all().values()
        total_categories=Category.objects.all().values()
        total_products=Product.objects.all().values()
        total_orders=Order.objects.all().values()
       
        total['total_brands']=len(total_brands)
        total['total_models']=len(total_models)
        total['total_categories']=len(total_categories)
        total['total_products']=len(total_products)
        total['total_orders']=len(total_orders)

        return Response(total,status=status.HTTP_200_OK)

