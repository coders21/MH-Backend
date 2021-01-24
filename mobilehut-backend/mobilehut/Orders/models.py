from django.db import models
from Products.models import Product
from authapp.models import User

# Order Models
class Order(models.Model):
    order_date=models.DateField(blank=True)
    order_status=models.CharField(max_length=20,blank=True)
    order_returndate=models.DateField(blank=True)

class ProductOrder(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    quantity=models.IntegerField(blank=True)