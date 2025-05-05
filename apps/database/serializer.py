from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UtilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Util
        fields = '__all__'

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'

class PurchaseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseDetail
        fields = '__all__'

class RequestDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestDetail
        fields = '__all__'

class UtilsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UtilsList
        fields = '__all__'

class ListDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListDetail
        fields = '__all__'

class MoneyDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = MoneyDelivery
        fields = '__all__'

class UtilsDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = UtilsDelivery
        fields = '__all__'

class UtilsDeliveryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UtilsDeliveryDetail
        fields = '__all__'