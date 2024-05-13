from rest_framework import serializers
from .models import YourModel, YourModel2, Instance


class YourModel2Serializer(serializers.ModelSerializer):
    class Meta:
        model = YourModel2
        fields = '__all__'


class YourModelSerializer(serializers.ModelSerializer):
    yourmodel2 = YourModel2Serializer()

    class Meta:
        model = YourModel
        fields = '__all__'


class InstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instance
        fields = '__all__'
