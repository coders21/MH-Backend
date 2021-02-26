from django.contrib import admin
from .models import Carousel,ThreeBanner,OneBanner,Sale,TrendingProductImage,ProductSale
# Register your models here.


admin.site.register(Carousel)
admin.site.register(ThreeBanner)
admin.site.register(OneBanner)
admin.site.register(Sale)
admin.site.register(TrendingProductImage)
admin.site.register(ProductSale)