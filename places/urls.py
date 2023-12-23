from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("type", views.PlaceTypeModelViewSet)
router.register("status", views.PlaceStatusModelViewSet)
router.register("place", views.PlaceModelViewSet)

urlpatterns = router.urls 