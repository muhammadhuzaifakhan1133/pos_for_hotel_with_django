from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter
from users.models import CustomerModel, UserCategoryModel, UserModel
from users.serializers import CustomerSerializer, UserCategorySerializer, UserSerializer
# from rest_framework.request import Request
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.views import APIView

class CustomerCustomSearchFilter(FilterSet):
    name_contains = CharFilter(field_name='name', lookup_expr="contains")
    phone_contains = CharFilter(field_name='phone', lookup_expr="contains")
    address_contains = CharFilter(field_name='address', lookup_expr="contains")
    email_contains = CharFilter(field_name='email', lookup_expr="contains")
    class Meta:
        model = CustomerModel
        fields = ['name_contains', 'phone_contains', 'address_contains', 'email_contains']


class CustomerModelViewSet(ModelViewSet):
    queryset = CustomerModel.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CustomerCustomSearchFilter

class UserCustomSearchFilter(FilterSet):
    name_contains = CharFilter(field_name='name', lookup_expr="contains")
    username_contains = CharFilter(field_name='username', lookup_expr="contains")
    class Meta:
        model = UserModel
        fields = ['name_contains', 'username_contains', ]


class UserModelViewSet(ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserCustomSearchFilter
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = [IsAuthenticated,]

class UserCategoryCustomSearchFilter(FilterSet):
    name_contains = CharFilter(field_name='name', lookup_expr="contains")
    class Meta:
        model = UserCategoryModel
        fields = ['name_contains']


class UserCategoryModelViewSet(ModelViewSet):
    queryset = UserCategoryModel.objects.all()
    serializer_class = UserCategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserCategoryCustomSearchFilter
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = [IsAuthenticated,]


# class LoginAPIView(APIView):
    
#     def post(self, request: Request):
#         if "username" not in request.data or "password" not in request.data:
#             return Response({
#                 "error": "Please enter username and password both"
#             }, status=status.HTTP_400_BAD_REQUEST)
#         user = UserModel.objects.filter(username=request.data.get("username"), password=request.data.get("password")).only().get()
#         if user is None:
#             return Response({
#                 "error": "Invalid username or password"
#             }, status=status.HTTP_400_BAD_REQUEST)
#         auth_user = User(username=user.username, password=user.password)
#         auth_user.save()
#         token, created = Token.objects.get_or_create(user=auth_user)
#         return Response({
#             "token": token.generate_key()
#         })
