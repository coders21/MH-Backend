from django.db import models
from authapp.models import User
from datetime import date

class Category(models.Model):
    category_name=models.CharField(max_length=50,blank=True)

class Brand(models.Model):
    brand_name=models.CharField(max_length=50,blank=True)
    brand_image=models.ImageField(upload_to="brand_images",null=True,blank=True)


class Product(models.Model):
    product_name=models.CharField(max_length=300,blank=True)
    product_price=models.IntegerField(blank=True)
    product_quantity=models.IntegerField(blank=True)
    product_sku=models.CharField(max_length=120,blank=True)
    product_description=models.CharField(max_length=5000,blank=True)
    sale_price=models.IntegerField(blank=True)
    saleprice_startdate=models.DateField(blank=True)
    saleprice_enddate=models.DateField(blank=True)
    product_reviews=models.FloatField(default=2,blank=True,null=True)
    review_count=models.IntegerField(default=3.9,blank=True,null=True)
    product_category=models.ForeignKey(Category,on_delete=models.CASCADE)
    product_brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    # product_model=models.ForeignKey(ModelType,on_delete=models.CASCADE)
    created_date=models.DateField(blank=True,null=True)
    category_name=models.CharField(max_length=50,null=True,blank=True)


class ModelType(models.Model):
    model_name=models.CharField(max_length=150,blank=True)
   

class ProductModel(models.Model):
    modelid=models.ForeignKey(ModelType,null=True,on_delete=models.CASCADE)
    model_product=models.CharField(max_length=150, blank=True)
    model_name=models.CharField(max_length=130,blank=True)

class Colour(models.Model):
    colour_name=models.CharField(max_length=20,blank=True)
    colour_product=models.ForeignKey(Product,on_delete=models.CASCADE)
   

class ProductImages(models.Model):
    image=models.ImageField(upload_to='product_images',null=True,blank=True)
    image_product=models.ForeignKey(Product,on_delete=models.CASCADE)



class ProductReviews(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=30,null=True,blank=True)
    description=models.CharField(max_length=200,null=True,blank=True)
    stars=models.FloatField(null=True,blank=True)
    review_image=models.ImageField(upload_to='review_images',null=True,blank=True)
    status=models.BooleanField(default=False,blank=True,null=True)
    date=models.DateField(default=date.today,null=True,blank=True)
    customername=models.CharField(max_length=50,null=True,blank=True)