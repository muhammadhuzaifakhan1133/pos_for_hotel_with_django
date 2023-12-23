from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter
from places.models import PlaceModel, PlaceStatusModel, PlaceTypeModel
from places.serializers import PlaceSerializer, PlaceStatusSerializer, PlaceTypeSerializer

class PlaceTypeCustomSearchFilter(FilterSet):
    name_contains = CharFilter(field_name='name', lookup_expr="contains")
    class Meta:
        model = PlaceTypeModel
        fields = ['name_contains']


class PlaceTypeModelViewSet(ModelViewSet):
    queryset = PlaceTypeModel.objects.all()
    serializer_class = PlaceTypeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PlaceTypeCustomSearchFilter

class PlaceStatusCustomSearchFilter(FilterSet):
    name_contains = CharFilter(field_name='name', lookup_expr="contains")
    class Meta:
        model = PlaceStatusModel
        fields = ['name_contains']


class PlaceStatusModelViewSet(ModelViewSet):
    queryset = PlaceStatusModel.objects.all()
    serializer_class = PlaceStatusSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PlaceStatusCustomSearchFilter

class PlaceCustomSearchFilter(FilterSet):
    name_contains = CharFilter(field_name='name', lookup_expr="contains")
    class Meta:
        model = PlaceModel
        fields = ['name_contains']


class PlaceModelViewSet(ModelViewSet):
    queryset = PlaceModel.objects.all()
    serializer_class = PlaceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PlaceCustomSearchFilter
