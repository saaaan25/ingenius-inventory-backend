# from django.shortcuts import render
# from django.http import JsonResponse
from apps.deliveries.models import Delivery, UtilDelivery, MoneyDelivery
from apps.api.serializers.deliveries import DeliverySerializer, MoneyDeliverySerializer, UtilDeliverySerializer
from rest_framework import generics

class Deliveries(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class DeliveryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    lookup_field = 'pk'

class UtilDeliveries(generics.ListCreateAPIView):
    queryset = UtilDelivery.objects.all()
    serializer_class = UtilDeliverySerializer

class UtilDeliveryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UtilDelivery.objects.all()
    serializer_class = UtilDeliverySerializer
    lookup_field = 'pk'

class MoneyDeliveries(generics.ListCreateAPIView):
    queryset = MoneyDelivery.objects.all()
    serializer_class = MoneyDeliverySerializer

class MoneyDeliveryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MoneyDelivery.objects.all()
    serializer_class = MoneyDeliverySerializer
    lookup_field = 'pk'