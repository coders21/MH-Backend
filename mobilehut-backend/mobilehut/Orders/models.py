from django.db import models
from Products.models import Product
from authapp.models import User

# Order Models
class Order(models.Model):
    order_date=models.DateField(blank=True)
    order_status=models.CharField(max_length=20,blank=True)
    order_returndate=models.DateField(blank=True,null=True)
    order_tracking=models.CharField(max_length=30,null=True,blank=True)
    shipping_provider=models.CharField(max_length=20,null=True,blank=True)
    update_date=models.DateField(blank=True,default='2021-01-26')
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class ProductOrder(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    quantity=models.IntegerField(blank=True)
    colour=models.CharField(max_length=40,default="green",blank=True)
    modelP=models.CharField(max_length=50,default="",blank=True)