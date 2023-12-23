from rest_framework import serializers
from places.models import PlaceModel, PlaceStatusModel, PlaceTypeModel


class PlaceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceTypeModel
        fields = "__all__"

class PlaceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceStatusModel
        fields = "__all__"

class PlaceSerializer(serializers.ModelSerializer):
    place_type_id = serializers.IntegerField()
    class Meta:
        model = PlaceModel
        fields = "__all__"
        depth = 1

    def create(self, validated_data):
        type_id = validated_data.pop('place_type_id')
        type_instance, created = PlaceTypeModel.objects.get_or_create(pk=type_id)
        status_instance, created = PlaceStatusModel.objects.get_or_create(pk=1)
        place_instance = PlaceModel.objects.create(**validated_data, place_status=status_instance, place_type=type_instance)
        return place_instance