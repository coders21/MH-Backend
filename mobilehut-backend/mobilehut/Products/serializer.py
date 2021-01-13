from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from .models import Product,Category,Brand,ModelType,Colour

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id','category_name']

    def create(self, validated_data):
        cat = Category.objects.create(**validated_data)
        return cat

    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)
            instance.save()
        return instance

class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ['id','brand_name']

    def create(self, validated_data):
        brnd = Brand.objects.create(**validated_data)
        return brnd

    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)
            instance.save()
        return instance

class ModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ModelType
        fields = ['id','model_name']

    def create(self, validated_data):
        model = ModelType.objects.create(**validated_data)
        return model

    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)
            instance.save()
        return instance

class ColourSerializer(serializers.ModelSerializer):

    class Meta:
        model = Colour
        fields = ['colour_name','colour_product','id']

    def create(self, validated_data):
        model = Colour.objects.create(**validated_data)
        return model

    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)
            instance.save()
        return instance

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id','product_name','product_sku','product_description','product_quantity','product_price','product_category','product_brand','product_model']

    def create(self, validated_data):
        pro = Product.objects.create(**validated_data)
        return pro

    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)
            instance.save()
        return instance

