from django.db import models
from products.models import ProductModel
from users.models import CustomerModel, UserModel

In_Dine = "IN_DINE"
Takeaway = "TAKEAWAY"
Delivery = "DELIVERY"

OrderTypeChoices = [
    (In_Dine, "IN_DINE"), (Takeaway, "TAKEAWAY"), (Delivery, "DELIVERY"),
]

class OrderModel(models.Model):
    name = models.CharField(max_length=200)
    remarks = models.CharField(max_length=200)
    price = models.FloatField()
    discount = models.FloatField(0)
    expense = models.FloatField(0)
    cusomter = models.ForeignKey(CustomerModel, on_delete=models.CASCADE, null=True),
    rider = models.ForeignKey(UserModel, null=True, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    order_type = models.CharField(max_length=8, choices=OrderTypeChoices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderDetailModel(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    order_quantity = models.IntegerField()
    order_price = models.FloatField()
    discount = models.FloatField(0)