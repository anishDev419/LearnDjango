from django.urls import path, include
from rest_framework import routers
from .views import YourModelViewSet

router = routers.DefaultRouter()
router.register(r'yourmodels', YourModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
