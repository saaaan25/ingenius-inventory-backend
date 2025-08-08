from rest_framework import serializers
from apps.utils.models import Util

class UtilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Util
        fields = '__all__'