from rest_framework import serializers
from .models import ProductCategoryModel, ProductModel

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategoryModel
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    product_category_id = serializers.IntegerField()
    class Meta:
        model = ProductModel
        fields = "__all__"
        depth = 1

    def create(self, validated_data):
        cat_id = validated_data.pop('product_category_id')
        product_category_instance, created = ProductCategoryModel.objects.get_or_create(pk=cat_id)
        product_instance = ProductModel.objects.create(**validated_data, product_category=product_category_instance)
        return product_instance

