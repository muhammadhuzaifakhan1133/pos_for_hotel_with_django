from rest_framework.routers import DefaultRouter
from . import views
# from django.urls import path

router = DefaultRouter()
router.register("customer", views.CustomerModelViewSet)
router.register("user", views.UserModelViewSet)
router.register("category", views.UserCategoryModelViewSet)

urlpatterns = router.urls \
# + [path("login", views.LoginAPIView.as_view())]