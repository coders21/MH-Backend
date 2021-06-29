from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from Products.models import Category,Product,ProductImages,Brand,ProductReviews,ProductModel,Colour
from rest_framework import status
from rest_framework import generics
from .models import Carousel,OneBanner,ThreeBanner,Sale,ProductSale,RecommendedProduct,TrendingProductImage
from .serializer import CarouselSerializer,OneBannerSerializer,ThreeBannerSerializer,SaleSerializer,RecommendedProductSerializer,ProductSaleSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from django.conf import settings
from django.db import connection, reset_queries
from datetime import datetime,timedelta,date
import random
from django.db.models import Q
from rest_framework.permissions import IsAuthenticatedOrReadOnly,BasePermission, SAFE_METHODS

class CreateCarousel(generics.ListCreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset=Carousel.objects.all()
    serializer_class=CarouselSerializer
    

class ManageCarousel(generics.RetrieveUpdateDestroyAPIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer
    lookup_field = 'pk'
    

class CreateThreeBanner(generics.ListCreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset=ThreeBanner.objects.all()
    serializer_class=ThreeBannerSerializer
    

class ManageThreeBanner(generics.RetrieveUpdateDestroyAPIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset = ThreeBanner.objects.all()
    serializer_class = ThreeBannerSerializer
    lookup_field = 'pk'
    

class CreateOneBanner(generics.ListCreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset=OneBanner.objects.all()
    serializer_class=OneBannerSerializer
    

class ManageOneBanner(generics.RetrieveUpdateDestroyAPIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset = OneBanner.objects.all()
    serializer_class = OneBannerSerializer
    lookup_field = 'pk'
    

class CreateSale(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset=Sale.objects.all()
    serializer_class=SaleSerializer
    

class ManageSale(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    lookup_field = 'pk'

class GetSaleProduct(APIView):

    def get(self,request,id):
        #reset=True
        prod=ProductSale.objects.filter(sale=id).select_related('product')
        sale_product=[]
        for prod in prod:
            sale_product.append({"product_id":prod.product.id,"product_name":prod.product.product_name,"product_price":prod.product.product_price,
            "sale_price":prod.product.sale_price,"saleprice_startdate":prod.product.saleprice_startdate,
            "saleprice_enddate":prod.product.saleprice_enddate,"stock":prod.product.product_quantity})
        
        sale_data={}
        sale_data['sale_product']=sale_product

        
        return Response(sale_data,status=status.HTTP_200_OK)


class CreateProductSale(APIView):

     permission_classes=[IsAuthenticatedOrReadOnly]

     def get(self,request):
         return Response([ProductSaleSerializer(dat).data for dat in ProductSale.objects.all()])
    
     def post(self,request):

        payload=request.data
       
        prod=list(ProductSale.objects.filter(sale=payload['sale']).prefetch_related('product'))
       
        sale_product=True
    
        for x in range(0,len(prod)):
            if prod[x].product.id == int(payload['product']):
                sale_product=False
                break
        
        if (sale_product):
            payload=request.data
            serializer = ProductSaleSerializer(data=payload)
            if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)                             
        else:
            return Response ("product already exist",status=status.HTTP_200_OK)
            


class ManageProductSale(APIView):
    
    # Removing product from sale
    permission_classes=[IsAuthenticatedOrReadOnly]
    def post (self,request,id):
        
        payload=request.data
        ps=ProductSale.objects.filter(sale=payload['sale']).filter(product=id)
        ps.delete()
        
        return Response ("Product Removed",status=status.HTTP_200_OK)
    

class CreateRecommendedProduct(APIView):

    permission_classes=[IsAuthenticatedOrReadOnly]
    def get(self,request):
         return Response([RecommendedProductSerializer(dat).data for dat in RecommendedProduct.objects.all()])
    
    def post(self,request):
        payload=request.data    
        try:
            rp=RecommendedProduct.objects.filter(product=payload['product'])
            
            if len(rp)>0:
                return Response("Product already exists",status=status.HTTP_200_OK)
            else:
                payload=request.data
                serializer = RecommendedProductSerializer(data=payload)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            pass
    

class ManageRecommendedProduct (generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset = RecommendedProduct.objects.all()
    serializer_class = RecommendedProductSerializer
    lookup_field = 'pk'
    

class GetHomeData(APIView):

    def get(self,request):
       
        # carousel=Carousel.objects.all().values()
        # main_banner_carousel={
        #     "carousel":carousel
        # }
        categories=Category.objects.all().values()
        
        homepagedata={}
        #homepagedata['carousel']=main_banner_carousel['carousel']
        homepagedata['category']=categories
        brands=Brand.objects.all().order_by('id')[:6].values()
        homepagedata['brands']=brands
        

        sale_product=[]
        save_val=True
        review_product=None
        try:
            sale=Sale.objects.get(startdate__lte=datetime.today().strftime('%Y-%m-%d'),enddate__gte=datetime.today().strftime('%Y-%m-%d'))
        except (KeyError, Sale.DoesNotExist):
            pass
        else:
            prod=ProductSale.objects.filter(sale=sale.id).select_related('product')
            for prod in prod:
                for x in range (0,len(sale_product)): # check duplicate
                        if prod.product.id==sale_product[x]['product_id']:
                            save_val=False
                            break
                if save_val:
                    pr=ProductReviews.objects.filter(product=prod.product_id).values()
                    pm=ProductModel.objects.filter(model_product=prod.product_id).values()
                    pc=Colour.objects.filter(colour_product=prod.product_id).values()
                    review_product=CalculateRating(pr)
                    images=prod.product.productimages_set.all().order_by('id')[:2].values()
                    sale_product.append({"product_id":prod.product.id,"product_name":prod.product.product_name,"stock":prod.product.product_quantity,"product_price":prod.product.product_price,
                    "sale_price":prod.product.sale_price,"saleprice_startdate":prod.product.saleprice_startdate,
                    "saleprice_enddate":prod.product.saleprice_enddate,"product_category":prod.product.category_name,"product_reviews":review_product,"review_count":len(pr),
                    "product_images":images,'product_colour':pc,'product_model':pm})
                save_val=True
            homepagedata['sale']={
                    "startdate":sale.startdate,
                    "enddate":sale.enddate,
                    "salename":sale.name,
                    "product":sale_product
            }

        one_banner=OneBanner.objects.all().values()
        homepagedata['one_banner']=one_banner
        # threebanner=ThreeBanner.objects.all().values()
        # three_banner={
        #     "banner":threebanner
        # }
        # homepagedata['three_banner']=three_banner['banner']
        
        prod=Product.objects.all().order_by('review_count')[:8]
        trend_products=[]
        for prod in prod:
            pr=ProductReviews.objects.filter(product=prod.id).values()
            pm=ProductModel.objects.filter(model_product=prod.id).values()
            pc=Colour.objects.filter(colour_product=prod.id).values()
            review_product=CalculateRating(pr)
            images=prod.productimages_set.all().order_by('id')[:2].values()
            trend_products.append({"product_id":prod.id,"product_name":prod.product_name,"stock":prod.product_quantity,"product_category":prod.category_name,"product_price":prod.product_price,
                "sale_price":prod.sale_price,"saleprice_startdate":prod.saleprice_startdate,
                "saleprice_enddate":prod.saleprice_enddate,"product_reviews":review_product,"review_count":len(pr),"product_images":images,'product_colour':pc,'product_model':pm})
       
        homepagedata['trending_products']=trend_products

        prod=RecommendedProduct.objects.all()[:8].select_related('product')
        recommended=[]
        for prod in prod:
            pr=ProductReviews.objects.filter(product=prod.product.id).values()
            pm=ProductModel.objects.filter(model_product=prod.product.id).values()
            pc=Colour.objects.filter(colour_product=prod.product.id).values()
            review_product=CalculateRating(pr)
            images=prod.product.productimages_set.all().order_by('id')[:2].values()
            recommended.append({"product_id":prod.product.id,"product_name":prod.product.product_name,"stock":prod.product.product_quantity,"product_category":prod.product.category_name,"product_price":prod.product.product_price,
                "sale_price":prod.product.sale_price,"saleprice_startdate":prod.product.saleprice_startdate,
                "saleprice_enddate":prod.product.saleprice_enddate,"product_reviews":review_product,"review_count":len(pr),"product_images":images,"product_colour":pc,"product_model":pm})
        homepagedata['recommended_product']=recommended

        
        prod=Product.objects.all().prefetch_related('productimages_set')
        new_arrival_product=[]
        for prod in prod:
            pr=ProductReviews.objects.filter(product=prod.id).values()
            pm=ProductModel.objects.filter(model_product=prod.id).values()
            pc=Colour.objects.filter(colour_product=prod.id).values()
            review_product=CalculateRating(pr)
            images=prod.productimages_set.all().order_by('id')[:2].values()
            new_arrival_product.append({"product_id":prod.id,"product_name":prod.product_name,"stock":prod.product_quantity,"product_category":prod.category_name,"product_price":prod.product_price,
                "sale_price":prod.sale_price,"saleprice_startdate":prod.saleprice_startdate,"created_date":prod.created_date,
                "saleprice_enddate":prod.saleprice_enddate,"product_reviews":review_product,"review_count":len(pr),"product_images":images,"product_colour":pc,"product_model":pm})
            
       
        select_new_arrival=[]
        
        for  x in range(0,len(new_arrival_product)):
            mydate=new_arrival_product[x]['created_date']
            mydate_limit = mydate + timedelta(days=+14)
            
            if date.today() < mydate_limit:
               select_new_arrival.append(new_arrival_product[x])
        
        if len(select_new_arrival)>7:
            random_products_arrival=random.sample(select_new_arrival,8)
        else:
            random_products_arrival=select_new_arrival

        homepagedata['new_arrival_product']=random_products_arrival

        # trend_image=TrendingProductImage.objects.all().values()
        # homepage['trending_image']=trend_image
        
        

        return Response(homepagedata,status=status.HTTP_200_OK)


def CalculateRating(pr):

    sum_rate=0
    count_rate=0
    for pr1 in pr:
        sum_rate=sum_rate+(pr1['stars'])
    
    count_rate=len(pr)

    if (count_rate==0):
        return 0
    else:
        return sum_rate/count_rate


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