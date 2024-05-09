from django.urls import path
from django.views.generic import TemplateView, RedirectView

from . import views
app_name="api"

urlpatterns = [
    path('', views.ApiTest.as_view(), name='api_test'),
]
