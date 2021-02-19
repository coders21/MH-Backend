from rest_framework import serializers
from .models import Carousel,ThreeBanner,OneBanner,Sale,ProductSale,RecommendedProduct

class CarouselSerializer(serializers.ModelSerializer):

    class Meta:
        model = Carousel
        fields = '__all__'

    def create(self, validated_data):
        carousel = Carousel.objects.create(**validated_data)
        return carousel

    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)
            instance.save()
        return instance


class ThreeBannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = ThreeBanner
        fields = '__all__'

    def create(self, validated_data):
        TB = ThreeBanner.objects.create(**validated_data)
        return TB

    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)
            instance.save()
        return instance
    
class OneBannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = OneBanner
        fields = '__all__'

    def create(self, validated_data):
        OB = OneBanner.objects.create(**validated_data)
        return OB

    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)
            instance.save()
        return instance


class SaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sale
        fields = '__all__'

    def create(self, validated_data):
        SS = Sale.objects.create(**validated_data)
        return SS

    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)
            instance.save()
        return instance


class ProductSaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductSale
        fields = '__all__'

    def create(self, validated_data):
        PS = ProductSale.objects.create(**validated_data)
        return PS

    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)
            instance.save()
        return instance

class RecommendedProductSerializer(serializers.ModelSerializer):

    product_name= serializers.StringRelatedField()
    product_category= serializers.StringRelatedField()
    product_sku= serializers.StringRelatedField()

    class Meta:
        model = RecommendedProduct
        fields = ['id','product','product_name','product_category','product_sku']

    def create(self, validated_data):
        RP = RecommendedProduct.objects.create(**validated_data)
        return RP

    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)
            instance.save()
        return instance
    
    def to_representation(self, instance):
        rep = super(RecommendedProductSerializer, self).to_representation(instance)
        rep['product_name'] = instance.product.product_name
        rep['product_category'] = instance.product.category_name
        rep['product_sku']= instance.product.product_sku
        return rep
