from django.shortcuts import render
from rest_framework import viewsets
from ..serializer import UtilsListSerializer
from ..models import UtilsList

class UtilsListView(viewsets.ModelViewSet):
    serializer_class = UtilsListSerializer
    queryset = UtilsList.objects.all()