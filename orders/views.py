from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter

from orders.models import OrderDetailModel, OrderModel
from orders.serializers import OrderDetailSerializer, OrderSerializer

class OrderCustomSearchFilter(FilterSet):
    name_contains = CharFilter(field_name='name', lookup_expr="contains")
    remarks_contains = CharFilter(field_name='remarks', lookup_expr="contains")
    price = CharFilter(field_name='price')
    quantity = CharFilter(field_name='quantity')
    discount = CharFilter(field_name='discount')
    expense = CharFilter(field_name='expense')
    is_paid = CharFilter(field_name='is_paid')
    class Meta:
        model = OrderModel
        fields = ['name_contains', 'remarks_contains', 'price', 'quantity', 'discount', 'expense', 'is_paid']


class OrderModelViewSet(ModelViewSet):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderCustomSearchFilter

class OrderDetailModelViewSet(ModelViewSet):
    queryset = OrderDetailModel.objects.all()
    serializer_class = OrderDetailSerializer