from django.urls import path, include
from rest_framework import routers
# from .views import YourModelViewSet
from .views import YourModelViewSet, test, YourModel2ViewSet, InstanceViewSet, RenewalTypeViewSet

router = routers.DefaultRouter()
router.register(r'RouterName', YourModelViewSet)
router.register(r'RouterName2', YourModel2ViewSet)
router.register(r'Instance', InstanceViewSet, basename='instance')
router.register(r'renewal', RenewalTypeViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('', include(router.urls)),
    # path('', test, name="test"),
]
