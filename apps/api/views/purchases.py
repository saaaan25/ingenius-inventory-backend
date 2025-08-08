from apps.purchases.models import Purchase, PurchaseDetail
from apps.api.serializers import PurchaseSerializer, PurchaseDetailSerializer
from rest_framework import generics

class Purchases(generics.ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class PurchaseDet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    lookup_field = 'pk'

class PurchaseDetails(generics.ListCreateAPIView):
    queryset = PurchaseDetail.objects.all()
    serializer_class = PurchaseDetailSerializer

class PurchaseDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseDetail.objects.all()
    serializer_class = PurchaseDetailSerializer
    lookup_field = 'pk'