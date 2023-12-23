from django.db import models

class UserCategoryModel(models.Model):
    name = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserModel(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    user_category = models.ForeignKey(UserCategoryModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CustomerModel(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    address = models.TextField()
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
