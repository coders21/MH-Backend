from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ProductSerializer,CategorySerializer,BrandSerializer,ModelSerializer,ColourSerializer
from .models import Product,Category,Brand,ModelType,Colour
from rest_framework import status

#### CATEGORY VIEWS ####

class CreateCategory(APIView):

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

    def get(self,request):
        return Response([ProductSerializer(dat).data for dat in Product.objects.all()])

    def post(self,request):
        payload=request.data
        serializer = ProductSerializer(data=payload)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ManageProduct(APIView):

    def get(self, request, id):

        try:
            pro = Product.objects.get(id=int(id))
        except (KeyError, Product.DoesNotExist):
            return Response('Product Not Found', status.HTTP_404_NOT_FOUND)
        else:
            serializer = ProductSerializer(pro)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):

        try:
            pro = Product.objects.get(id=int(id))
        except (KeyError, Product.DoesNotExist):
            return Response('Product Not Found', status.HTTP_404_NOT_FOUND)
        else:
            payload = request.data
            serializer = ProductSerializer(pro,data=payload)

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