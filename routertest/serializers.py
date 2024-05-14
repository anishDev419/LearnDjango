from rest_framework import serializers
from .models import YourModel, YourModel2, Instance, Renewal_Type


class YourModel2Serializer(serializers.ModelSerializer):
    class Meta:
        model = YourModel2
        fields = '__all__'


class YourModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourModel
        fields = '__all__'


class RenewalTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Renewal_Type
        fields = '__all__'


class InstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instance
        fields = '__all__'

    def validate(self, attrs):
        print(attrs)
        return attrs