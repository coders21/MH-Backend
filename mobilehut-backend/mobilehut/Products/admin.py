from django.contrib import admin
from .models import Product,Category,ModelType,Brand,Colour,ProductImages

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ModelType)
admin.site.register(Brand)
admin.site.register(Colour)
admin.site.register(ProductImages)