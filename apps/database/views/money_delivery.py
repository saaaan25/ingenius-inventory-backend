from django.shortcuts import render
from rest_framework import viewsets
from ..serializer import MoneyDeliverySerializer
from ..models import MoneyDelivery

class MoneyDeliveryView(viewsets.ModelViewSet):
    serializer_class = MoneyDeliverySerializer
    queryset = MoneyDelivery.objects.all()