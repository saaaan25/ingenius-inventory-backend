from rest_framework import serializers
from apps.deliveries.models import Delivery, UtilDelivery, MoneyDelivery

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'

class UtilDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = UtilDelivery
        fields = '__all__'

class MoneyDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = MoneyDelivery
        fields = '__all__'