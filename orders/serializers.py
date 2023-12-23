from rest_framework import serializers
from places.models import PlaceModel
from products.models import ProductModel

from users.models import CustomerModel, UserModel
from .models import OrderModel, OrderDetailModel


class OrderSerializer(serializers.ModelSerializer):
    customer_id = serializers.IntegerField()
    rider_id = serializers.IntegerField()
    place_id = serializers.IntegerField()
    class Meta:
        model = OrderModel
        fields = "__all__"

    def create(self, validated_data):
        customer_instance=None
        rider_instance = None
        if validated_data.get("customer_id") != None:
            cust_id = validated_data.pop('customer_id')
            customer_instance, created = CustomerModel.objects.get_or_create(pk=cust_id)
        if validated_data.get("rider_id") != None:
            rd_id = validated_data.pop('rider_id')
            rider_instance, created = UserModel.objects.get_or_create(pk=rd_id)
        pl_id = validated_data.pop("place_id")
        place_instance = PlaceModel.objects.get(pk=pl_id)
        order_instance = OrderModel.objects.create(**validated_data, rider=rider_instance, customer=customer_instance)
        place_instance.order = order_instance
        place_instance.save()
        return order_instance

class OrderDetailSerializer(serializers.ModelSerializer):
    order_id = serializers.IntegerField()
    product_id = serializers.IntegerField()
    
    class Meta:
        model = OrderModel
        fields = "__all__"

    def create(self, validated_data):
        od_id = validated_data.pop('order_id')
        order_instance, created = OrderModel.objects.get_or_create(pk=od_id)
        pod_id = validated_data.pop('product_id')
        product_instance, created = ProductModel.objects.get_or_create(pk=pod_id)
        
        order_detail_instance = OrderModel.objects.create(**validated_data, order=order_instance, product=product_instance)
        
        return order_detail_instance
