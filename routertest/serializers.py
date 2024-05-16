from datetime import datetime, timedelta

from rest_framework import serializers
from .models import YourModel, YourModel2, Instance, Renewal_Type
from django.utils import timezone


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

    def to_internal_value(self, data):
        new_data = data.copy()
        renew_type_id = data.get('renewal_type')
        renew_type = Renewal_Type.objects.get(pk=renew_type_id)

        if self.instance:
            print("UPDATING")

            instance = self.instance

        else:
            print("CREATING")

            if 'recent_renew_date' not in data:
                new_data['recent_renew_date'] = timezone.now().date().strftime("%Y-%m-%d")

        # CALCULATE EXPIRY DATE
        recent_renew_date_delta = datetime.strptime(new_data['recent_renew_date'], '%Y-%m-%d')
        expiry_date = recent_renew_date_delta + timedelta(days=renew_type.no_of_days)
        new_data['expiry_date'] = expiry_date.strftime('%Y-%m-%d')

        return super().to_internal_value(new_data)
