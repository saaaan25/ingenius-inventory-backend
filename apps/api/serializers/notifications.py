from rest_framework import serializers
from apps.notifications.models import Notification, Addressee

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class AdresseeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addressee
        fields = '__all__'  