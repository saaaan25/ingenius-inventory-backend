from django.shortcuts import render
from rest_framework import viewsets
from ..serializer import DeliverySerializer
from ..models import Delivery

class DeliveryView(viewsets.ModelViewSet):
    serializer_class = DeliverySerializer
    queryset = Delivery.objects.all()