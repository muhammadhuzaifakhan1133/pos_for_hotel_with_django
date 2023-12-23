from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("order", views.OrderModelViewSet)
router.register("detail", views.OrderDetailModelViewSet)

urlpatterns = router.urls 