from django.db import models
from Products.models import Product
# Create your models here.

class Carousel(models.Model):
    image=models.ImageField(upload_to='main_carousel',blank=True,null=True)
    title=models.CharField(max_length=100,null=True,blank=True)
    subtitle=models.CharField(max_length=50,null=True,blank=True)
    price=models.CharField(max_length=40,null=True,blank=True)
    carousel_link=models.CharField(max_length=500,null=True,blank=True)


class ThreeBanner(models.Model):
    image=models.ImageField(upload_to='three_banner',blank=True,null=True)
    subtitle=models.CharField(max_length=50,blank=True,null=True)
    bannertitle=models.CharField(max_length=50,blank=True,null=True)
    lighttext=models.CharField(max_length=50,blank=True,null=True)
    link=models.CharField(max_length=500,blank=True,null=True)


class OneBanner(models.Model):
    image=models.ImageField(upload_to='one_banner',blank=True,null=True)
    text=models.CharField(max_length=50,null=True,blank=True)
    price=models.CharField(max_length=40,null=True,blank=True)
    link=models.CharField(max_length=500,null=True,blank=True)


class Sale(models.Model):
    name=models.CharField(max_length=30,null=True,blank=True)
    startdate=models.DateField(null=True,blank=True)
    enddate=models.DateField(null=True,blank=True)


class ProductSale(models.Model):
    sale=models.ForeignKey(Sale,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)


class RecommendedProduct(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)


class TrendingProductImage(models.Model):
    trend_image=models.ImageField(upload_to="TrendingProductImage",null=True,blank=True)