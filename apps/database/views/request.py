from django.shortcuts import render
from rest_framework import viewsets
from ..serializer import RequestSerializer
from ..models import Request

class RequestView(viewsets.ModelViewSet):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()