from .models import Order,ProductOrder
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        order_check = Order.objects.create(**validated_data)
        return order_check

    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)
            instance.save()
        return instance

class ProductOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductOrder
        fields ='__all__'

    def create(self, validated_data):
        Pordr = ProductOrder.objects.create(**validated_data)
        return Pordr

    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)
            instance.save()
        return instance