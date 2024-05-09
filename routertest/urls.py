from django.urls import path, include
from rest_framework import routers
# from .views import YourModelViewSet
from .views import YourModelViewSet, test

router = routers.DefaultRouter()
router.register(r'RouterName', YourModelViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('', include(router.urls)),
    # path('', test, name="test"),
]
