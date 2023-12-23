from rest_framework import serializers
from .models import CustomerModel, UserCategoryModel, UserModel

class UserCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCategoryModel
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    user_category_id = serializers.IntegerField()
    class Meta:
        model = UserModel
        fields = "__all__"
        depth = 1

    def create(self, validated_data):
        user_category_id = validated_data.pop('user_category_id')
        user_category_instance, created = UserCategoryModel.objects.get_or_create(pk=user_category_id)
        user_instance = UserModel.objects.create(**validated_data, user_category=user_category_instance)
        return user_instance

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = "__all__"
