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
        reset=True
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
        main_banner_carousel={
            "carousel":
            [
                {
                    "image":"product_images/main.png"
                },
                {
                    "image":"product_images/main.png"
                }
            ]
        }


        categories=Category.objects.all().values()
        
        homepagedata={}
        homepagedata['carousel']=main_banner_carousel['carousel']
        homepagedata['category']=categories
        brands=Brand.objects.all().order_by('id')[:6].values()
        homepagedata['brands']=brands
        prod=Product.objects.filter().order_by('id')[:2].prefetch_related('productimages_set')
        flash_product=[]
       
        for prod in prod:
            images=prod.productimages_set.all().order_by('id')[:2].values()
            # check of start date and end date
            flash_product.append({"product_name":prod.product_name,"product_price":prod.product_price,
            "sale_price":prod.sale_price,"saleprice_startdate":prod.saleprice_startdate,
            "saleprice_enddate":prod.saleprice_enddate,"product_reviews":4.5,"review_count":2,
            "product_images":images})
        
        homepagedata['flashsale']={
            "enddate":"2019-09-02",
            "product":flash_product
        }
        
        homepagedata['one_banner']="product_images/main.png"


        three_banner={
            "banner":[
                 {
                    "image":"product_images/main.png"
                },
                {
                    "image":"product_images/main.png"
                }
                ,
                {
                    "image":"product_images/main.png"
                }
            ]
        }

        homepagedata['three_banner']=three_banner['banner']
        homepagedata['trending_products']=flash_product
        homepagedata['new_arrival_product']=flash_product

       
    

        return Response(homepagedata,status=status.HTTP_200_OK)
