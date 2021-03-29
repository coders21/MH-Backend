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
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    # if user order without creating account use below fields else use user info
    customername=models.CharField(max_length=30,null=True,blank=True)
    customeremail=models.CharField(max_length=40,null=True,blank=True)
    customercity=models.CharField(max_length=20,null=True,blank=True)
    customerprovince=models.CharField(max_length=30,null=True,blank=True)
    customeraddress=models.CharField(max_length=150,null=True,blank=True)
    customerphonenumber=models.CharField(max_length=30,null=True,blank=True)

class ProductOrder(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    quantity=models.IntegerField(blank=True)
    colour=models.CharField(max_length=40,default="green",blank=True)
    modelP=models.CharField(max_length=50,default="",blank=True)