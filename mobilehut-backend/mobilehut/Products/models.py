from django.db import models


class Category(models.Model):
    category_name=models.CharField(max_length=50,blank=True)

class Brand(models.Model):
    brand_name=models.CharField(max_length=50,blank=True)

class ModelType(models.Model):
    model_name=models.CharField(max_length=150,blank=True)

class Product(models.Model):
    product_name=models.CharField(max_length=300,blank=True)
    product_price=models.IntegerField(blank=True)
    product_quantity=models.IntegerField(blank=True)
    product_sku=models.CharField(max_length=120,blank=True)
    product_description=models.CharField(max_length=5000,blank=True)
    #product_reviews=models.FloatField(blank=True)
    product_category=models.ForeignKey(Category,on_delete=models.CASCADE)
    product_brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    product_model=models.ForeignKey(ModelType,on_delete=models.CASCADE)

# class ProductImages(models.Model):
#     image_name=models.ImageField(blank=True)
#     image_product=models.ForeignKey(Product,on_delete=models.CASCADE)

class Colour(models.Model):
    colour_name=models.CharField(max_length=20,blank=True)
    colour_product=models.ForeignKey(Product,on_delete=models.CASCADE)

