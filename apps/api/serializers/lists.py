from rest_framework import serializers
from apps.lists.models import List, ListDetail

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = "__all__"

class ListDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListDetail
        fields = "__all__"