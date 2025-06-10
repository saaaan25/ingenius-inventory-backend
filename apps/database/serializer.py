from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']
        extra_kwargs = {'password': {'write_only': True}}

class CollaboratorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    role = serializers.SlugRelatedField(read_only=True, slug_field='name')
    
    class Meta:
        model = Collaborator
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        return Collaborator.objects.create(user=user, **validated_data)

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