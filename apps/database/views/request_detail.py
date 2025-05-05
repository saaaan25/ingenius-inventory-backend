from django.shortcuts import render
from rest_framework import viewsets
from ..serializer import RequestDetailSerializer
from ..models import RequestDetail

class RequestDetailView(viewsets.ModelViewSet):
    serializer_class = RequestDetailSerializer
    queryset = RequestDetail.objects.all()