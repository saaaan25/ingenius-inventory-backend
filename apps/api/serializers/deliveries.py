from rest_framework import serializers
from apps.deliveries.models import Delivery

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'