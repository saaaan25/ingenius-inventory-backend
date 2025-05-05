from django.shortcuts import render
from rest_framework import viewsets
from ..serializer import PurchaseSerializer
from ..models import Purchase

class PurchaseView(viewsets.ModelViewSet):
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()