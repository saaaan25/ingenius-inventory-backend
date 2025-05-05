from django.shortcuts import render
from rest_framework import viewsets
from ..serializer import PurchaseDetailSerializer
from ..models import PurchaseDetail

class PurchaseDetailView(viewsets.ModelViewSet):
    serializer_class = PurchaseDetailSerializer
    queryset = PurchaseDetail.objects.all()