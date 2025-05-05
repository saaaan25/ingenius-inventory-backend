from django.shortcuts import render
from rest_framework import viewsets
from ..serializer import UtilsDeliveryDetailSerializer
from ..models import UtilsDeliveryDetail

class UtilsDeliveryDetailView(viewsets.ModelViewSet):
    serializer_class = UtilsDeliveryDetailSerializer
    queryset = UtilsDeliveryDetail.objects.all()