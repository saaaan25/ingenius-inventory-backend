from apps.deliveries.models import Delivery, UtilDelivery, MoneyDelivery
from apps.api.serializers import DeliverySerializer, MoneyDeliverySerializer, UtilDeliverySerializer
from rest_framework import generics
from apps.api.filters import DeliveryFilter, UtilDeliveryFilter, MoneyDeliveryFilter

class Deliveries(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    filterset_class = DeliveryFilter

class DeliveryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    lookup_field = 'pk'

class UtilDeliveries(generics.ListCreateAPIView):
    queryset = UtilDelivery.objects.all()
    serializer_class = UtilDeliverySerializer
    filterset_class = UtilDeliveryFilter

class UtilDeliveryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UtilDelivery.objects.all()
    serializer_class = UtilDeliverySerializer
    lookup_field = 'pk'

class MoneyDeliveries(generics.ListCreateAPIView):
    queryset = MoneyDelivery.objects.all()
    serializer_class = MoneyDeliverySerializer
    filterset_class = MoneyDeliveryFilter

class MoneyDeliveryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MoneyDelivery.objects.all()
    serializer_class = MoneyDeliverySerializer
    lookup_field = 'pk'