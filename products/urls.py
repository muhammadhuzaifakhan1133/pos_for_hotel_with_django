from rest_framework.routers import DefaultRouter
from . import views
# from django.urls import path

router = DefaultRouter()
router.register("product", views.ProductModelViewSet)
router.register("category", views.ProductCategoryModelViewSet)

urlpatterns = router.urls \
# + [path("login", views.LoginAPIView.as_view())]