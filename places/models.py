from django.db import models

from orders.models import OrderModel

class PlaceTypeModel(models.Model):
    name = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PlaceStatusModel(models.Model):
    name = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PlaceModel(models.Model):
    name = models.CharField(max_length=200, unique=True)
    place_type = models.ForeignKey(PlaceTypeModel, on_delete=models.CASCADE)
    place_status = models.ForeignKey(PlaceStatusModel, on_delete=models.CASCADE)
    order = models.ForeignKey(OrderModel, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)