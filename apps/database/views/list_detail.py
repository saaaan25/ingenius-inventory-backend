from django.shortcuts import render
from rest_framework import viewsets
from ..serializer import ListDetailSerializer
from ..models import ListDetail

class ListDetailView(viewsets.ModelViewSet):
    serializer_class = ListDetailSerializer
    queryset = ListDetail.objects.all()