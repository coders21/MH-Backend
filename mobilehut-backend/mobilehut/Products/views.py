from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ProductSerializer,CategorySerializer,BrandSerializer,ModelSerializer,ColourSerializer,ProductImgSerializer
from .models import Product,Category,Brand,ModelType,Colour,ProductImages,ProductModel
from .ProductList import getcategoryProducts,getbrandProducts,getunder99Products,getclearanceProducts,getbuyerpickProducts,getsaleProducts,getnewarrivalProducts,gettrendingProducts,getrecommendedProducts
from rest_framework.permissions import IsAuthenticated
from Orders.models import Order
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from datetime import datetime
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
    parser_classes = (MultiPartParser, FormParser)
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
    parser_classes = (MultiPartParser, FormParser)

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
        payload['created_date']=datetime.today().strftime('%Y-%m-%d')
        serializer = ProductSerializer(data=payload)

        if serializer.is_valid():
            serializer.save()         
            category=Category.objects.get(id=serializer.data['product_category'])
            productobj=Product.objects.get(id=serializer.data['id'])
            productobj.category_name=category.category_name
            productobj.save()
            #now save colour 
            for x in payload['product_colors']:
                Colour.objects.create(colour_name=x['name'],colour_product=productobj)
            # now save models
            for x in payload['product_models']:
                pmodel=ModelType.objects.get(id=x['id'])
                ProductModel.objects.create(modelid=pmodel,model_product=productobj,model_name=x['model_name'])

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
            model=ProductModel.objects.filter(model_product=pro.id).values()

            select_colour={}
            append_color=[]
            select_model={}
            append_model=[]

            for x in range(0,len(colour)):
                select_colour['id']=colour[x]['colour_name']
                select_colour['name']=colour[x]['colour_name']
                append_color.append(select_colour)
                select_colour={}
            
            
            for x in range(0,len(model)):
                select_model['model_name']=model[x]['model_name']
                select_model['id']=model[x]['id']
                append_model.append(select_model)
                select_model={}
            
            
            product_data=serializer.data
            product_data['product_colors']=append_color
            product_data['product_models']=append_model
            
            print(product_data)
            
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
            
            try:
                mdl=ProductModel.objects.filter(model_product=pro.id)
                mdl.delete()
            except:
                pass
            

            #now save colour 
            for x in payload['product_colors']:
                Colour.objects.create(colour_name=x['name'],colour_product=pro)
            
            #now save model

            for x in payload['product_models']:
                try:
                    pmodel=ModelType.objects.get(model_name=x['model_name'])
                    ProductModel.objects.create(modelid=pmodel,model_name=x['model_name'],model_product=pro.id)
                except:
                    pass

            if serializer.is_valid():
                serializer.save()
                category=Category.objects.get(id=serializer.data['product_category'])
                productobj=Product.objects.get(id=serializer.data['id'])
                productobj.category_name=category.category_name
                productobj.save()
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



class DetailProduct(APIView):

    def get(self,request,id):

        product_obj=Product.objects.get(id=id)
        product_img=ProductImages.objects.filter(image_product=product_obj.id).values()
        product_colour=Colour.objects.filter(colour_product=product_obj.id).values()
        product_model=ProductModel.objects.filter(model_product=product_obj.id).values()


        detail_product={
            "product_name":product_obj.product_name,
            "product_brand":product_obj.product_brand.brand_name,
            "product_category":product_obj.category_name,
            "product_quantity":product_obj.product_quantity,
            "product_sku":product_obj.product_sku,
            "product_price":product_obj.product_price,
            "sale_price":product_obj.sale_price,
            "product_description":product_obj.product_description,
            "product_reviews":product_obj.product_reviews,
            "review_count":product_obj.review_count,
            "saleprice_startdate":product_obj.saleprice_startdate,
            "saleprice_enddate":product_obj.saleprice_enddate,
            "product_images":product_img,
            "product_colour":product_colour,
            "product_model":product_model,
            "stock":product_obj.product_quantity
        }



        return Response(detail_product,status=status.HTTP_200_OK)



class ProductList(APIView):

    def post(self,request):
        select_type=request.data['type']
        show_data=None

        if (select_type=="category"): # shows all products of specific category
            show_data=getcategoryProducts(request.data['id'])
        elif (select_type=="brand"): # shows all products of specific brand
            show_data=getbrandProducts(request.data['id'])
        elif (select_type=="under99"): # shows all products of under 99 rs
            show_data=getunder99Products()
        elif (select_type=="clearance"):
            show_data=getclearanceProducts()
        elif (select_type=="buyer_picks"):
            show_data=getbuyerpickProducts()
        elif (select_type=="sale"):
            show_data=getsaleProducts()
        elif (select_type=="new_arrival"):
            show_data=getnewarrivalProducts()
        elif (select_type=="trending_product"):
            show_data=gettrendingProducts()
        elif (select_type=="recommended"):
            show_data=getrecommendedProducts()
        return Response(show_data,status=status.HTTP_200_OK)




