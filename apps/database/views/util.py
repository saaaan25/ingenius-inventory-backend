from django.shortcuts import render
from rest_framework import viewsets
from ..serializer import UtilSerializer
from ..models import Util

class UtilView(viewsets.ModelViewSet):
    serializer_class = UtilSerializer
    queryset = Util.objects.all()