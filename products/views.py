from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter
from products.models import ProductModel, ProductCategoryModel
from products.serializers import ProductSerializer, ProductCategorySerializer

class ProductCustomSearchFilter(FilterSet):
    name_contains = CharFilter(field_name='name', lookup_expr="contains")
    class Meta:
        model = ProductModel
        fields = ['name_contains']


class ProductModelViewSet(ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductCustomSearchFilter

class ProductCategoryCustomSearchFilter(FilterSet):
    name_contains = CharFilter(field_name='name', lookup_expr="contains")
    class Meta:
        model = ProductCategoryModel
        fields = ['name_contains']


class ProductCategoryModelViewSet(ModelViewSet):
    queryset = ProductCategoryModel.objects.all()
    serializer_class = ProductCategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductCategoryCustomSearchFilter