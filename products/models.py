from django.db import models

# Create your models here.
class ProductCategoryModel(models.Model):
    name = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ProductModel(models.Model):
    name = models.CharField(max_length=200, unique=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    product_category = models.ForeignKey(ProductCategoryModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)