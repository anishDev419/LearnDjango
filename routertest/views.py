from decouple import config
from django.contrib.auth.models import User
from django.shortcuts import render

from rest_framework import permissions, viewsets
from django.views.generic import TemplateView, DetailView, ListView, FormView, CreateView, UpdateView
from django.utils import timezone

from .models import YourModel, YourModel2, Instance, Renewal_Type
from .serializers import YourModelSerializer, InstanceSerializer, YourModel2Serializer, RenewalTypeSerializer


# Create your views here.
def test(request):
    template_name = "api/api_test.html"
    # Your view logic here
    return render(request, template_name)


class YourModel2ViewSet(viewsets.ModelViewSet):
    queryset = YourModel2.objects.all()
    serializer_class = YourModel2Serializer

    def list(self, request, *args, **kwargs):
        print(self.queryset)

        return super().list(self, request, *args, **kwargs)


# class InstanceViewSet(viewsets.ModelViewSet):
#     queryset = Instance.objects.all()
#     serializer_class = InstanceSerializer
#
#     def list(self, request, *args, **kwargs):
#         print("HELLO WORLD")
#
#         queryset = self.get_queryset()
#         print(queryset)
#
#         for instance in queryset:
#             print("HERE")
#             print(instance.id)
#             print(instance.name)
#
#         return super().list(request, *args, **kwargs)
#
#     def perform_create(self, serializer):
#         print("ADD PERFORM")
#         request_data = self.request.data
#         print('request_data: ', request_data)
#         queryset = self.queryset
#         print('queryset: ', queryset)
#         serializer.save()


class YourModelViewSet(viewsets.ModelViewSet):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer

    def update(self, request, *args, **kwargs):
        print("Custom update logic here")

        model1_serializer = YourModelSerializer()
        model2_serializer = YourModel2Serializer()
        print('model1_serializer', model1_serializer)
        print('model2_serializer', model2_serializer)

        # model1_instance = model1_serializer.save()
        # model2_instance = model2_serializer.save()

        # Call the update method of the parent class
        return super().update(request, *args, **kwargs)


class RenewalTypeViewSet(viewsets.ModelViewSet):
    queryset = Renewal_Type.objects.all()
    serializer_class = RenewalTypeSerializer


class InstanceViewSet(viewsets.ModelViewSet):
    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer

    def perform_create(self, serializer):
        print(" no mo teas")
        instance = serializer.save()

        instance.date_of_admission = timezone.now().date().strftime("%Y-%m-%d")

        # ADDING NEW USER
        # Generate a unique identifier for username
        unique_identifier = timezone.now().strftime("%Y%m%d%H%M%S")
        username = f'{instance.name}_user_{unique_identifier}'
        password = config('default_password')

        new_user = User(username=username, email=instance.email, first_name=instance.name, last_name='admin')
        new_user.set_password(password)
        print("new_user: ", new_user)
        new_user.save()

        serializer.save()

    def perform_update(self, serializer):
        instance = self.get_object()
        updated_instance = serializer.save()

        if updated_instance.renewal_type != instance.renewal_type:
            print("NOT THE SAME")
        else:
            print("THE SAME")

        serializer.save()
