from rest_framework import serializers
from apps.notifications.models import Notification, Adressee

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class AdresseeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adressee
        fields = '__all__'  