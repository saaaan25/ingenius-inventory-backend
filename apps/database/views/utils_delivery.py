from django.shortcuts import render
from rest_framework import viewsets
from ..serializer import UtilsDeliverySerializer
from ..models import UtilsDelivery

class UtilsDeliveryView(viewsets.ModelViewSet):
    serializer_class = UtilsDeliverySerializer
    queryset = UtilsDelivery.objects.all()