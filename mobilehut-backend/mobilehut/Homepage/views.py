from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from Products.models import Category,Product,ProductImages,Brand
from rest_framework import status
from rest_framework import generics
from .models import Carousel,OneBanner,ThreeBanner,Sale,ProductSale,RecommendedProduct
from .serializer import CarouselSerializer,OneBannerSerializer,ThreeBannerSerializer,SaleSerializer,RecommendedProductSerializer,ProductSaleSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from django.conf import settings
from django.db import connection, reset_queries
from datetime import datetime
import random

class CreateCarousel(generics.ListCreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset=Carousel.objects.all()
    serializer_class=CarouselSerializer
    

class ManageCarousel(generics.RetrieveUpdateDestroyAPIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer
    lookup_field = 'pk'
    

class CreateThreeBanner(generics.ListCreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset=ThreeBanner.objects.all()
    serializer_class=ThreeBannerSerializer
    

class ManageThreeBanner(generics.RetrieveUpdateDestroyAPIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset = ThreeBanner.objects.all()
    serializer_class = ThreeBannerSerializer
    lookup_field = 'pk'
    

class CreateOneBanner(generics.ListCreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset=OneBanner.objects.all()
    serializer_class=OneBannerSerializer
    

class ManageOneBanner(generics.RetrieveUpdateDestroyAPIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset = OneBanner.objects.all()
    serializer_class = OneBannerSerializer
    lookup_field = 'pk'
    

class CreateSale(generics.ListCreateAPIView):
    queryset=Sale.objects.all()
    serializer_class=SaleSerializer
    

class ManageSale(generics.RetrieveUpdateDestroyAPIView):
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
            "saleprice_enddate":prod.product.saleprice_enddate})
        
        sale_data={}
        sale_data['sale_product']=sale_product

        # print(len(connection.queries))

        # if reset:
        #     reset_queries()

       
        
        return Response(sale_data,status=status.HTTP_200_OK)


class CreateProductSale(generics.ListCreateAPIView):
    queryset=ProductSale.objects.all()
    serializer_class=ProductSaleSerializer

class ManageProductSale(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductSale.objects.all()
    serializer_class = ProductSaleSerializer
    lookup_field = 'pk'
    

class CreateRecommendedProduct(generics.ListCreateAPIView):
    queryset=RecommendedProduct.objects.all()
    serializer_class=RecommendedProductSerializer
    

class ManageRecommendedProduct (generics.RetrieveUpdateDestroyAPIView):
    queryset = RecommendedProduct.objects.all()
    serializer_class = RecommendedProductSerializer
    lookup_field = 'pk'
    

class GetHomeData(APIView):

    def get(self,request):
        carousel=Carousel.objects.all().values()
        main_banner_carousel={
            "carousel":carousel
        }
        categories=Category.objects.all().values()
        
        homepagedata={}
        homepagedata['carousel']=main_banner_carousel['carousel']
        homepagedata['category']=categories
        brands=Brand.objects.all().order_by('id')[:8].values()
        homepagedata['brands']=brands
        #prod=Product.objects.filter().order_by('id')[:2].prefetch_related('productimages_set')
        sale_product=[]
        try:
            sale=Sale.objects.get(startdate__lte=datetime.today().strftime('%Y-%m-%d'),enddate__gte=datetime.today().strftime('%Y-%m-%d'))
        except (KeyError, Sale.DoesNotExist):
            pass
        else:
            prod=ProductSale.objects.filter(sale=sale.id).select_related('product')
            for prod in prod:
                sale_product.append({"product_id":prod.product.id,"product_name":prod.product.product_name,"product_price":prod.product.product_price,
                "sale_price":prod.product.sale_price,"saleprice_startdate":prod.product.saleprice_startdate,
                "saleprice_enddate":prod.product.saleprice_enddate,"product_review":prod.product.product_reviews,"review_count":prod.product.review_count})
                homepagedata['sale']={
                    "startdate":sale.startdate,
                    "enddate":sale.enddate,
                    "salename":sale.name,
                    "product":sale_product
                 }
        

        one_banner=OneBanner.objects.all().values()
        homepagedata['one_banner']=one_banner
        threebanner=ThreeBanner.objects.all().values()
        three_banner={
            "banner":threebanner
        }
        homepagedata['three_banner']=three_banner['banner']
        
        trend_products=Product.objects.all().order_by('review_count')[:8].values()
        homepagedata['trending_products']=trend_products

        prod=RecommendedProduct.objects.all()[:8].select_related('product')
        recommended=[]
        for prod in prod:
            recommended.append({"product_id":prod.product.id,"product_name":prod.product.product_name,"product_price":prod.product.product_price,
                "sale_price":prod.product.sale_price,"saleprice_startdate":prod.product.saleprice_startdate,
                "saleprice_enddate":prod.product.saleprice_enddate,"product_review":prod.product.product_reviews,"review_count":prod.product.review_count})
        homepagedata['recommended_product']=recommended

        
        new_arrival_product=Product.objects.all().values()
        select_new_arrival=[]

        for new_arrival_product in new_arrival_product:
            mydate=new_arrival_product['created_date']
            if mydate.strftime("%m")==datetime.today().strftime("%m"):
               select_new_arrival.append(new_arrival_product)
        
        if len(select_new_arrival)>7:
            random_products_arrival=random.sample(select_new_arrival,8)
        else:
            random_products_arrival=select_new_arrival

        homepagedata['new_arrival_product']=random_products_arrival

       
    

        return Response(homepagedata,status=status.HTTP_200_OK)
