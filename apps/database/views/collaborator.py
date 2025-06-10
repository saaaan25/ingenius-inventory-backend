from django.shortcuts import render
from rest_framework import viewsets
from ..serializer import CollaboratorSerializer
from ..models import Collaborator

class CollaboratorView(viewsets.ModelViewSet):
    serializer_class = CollaboratorSerializer
    queryset = Collaborator.objects.all()