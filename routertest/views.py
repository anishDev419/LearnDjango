from django.shortcuts import render

from rest_framework import permissions, viewsets
from django.views.generic import TemplateView, DetailView, ListView, FormView, CreateView, UpdateView

from .models import YourModel
from .serializers import YourModelSerializer


# Create your views here.
def test(request):
    template_name = "api/api_test.html"
    # Your view logic here
    return render(request, template_name)


class YourModelViewSet(viewsets.ModelViewSet):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer