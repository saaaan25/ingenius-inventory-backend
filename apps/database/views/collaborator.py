from django.shortcuts import render
from rest_framework import viewsets
from ..serializer import CollaboratorSerializer
from ..models import Collaborator

class CollaboratorView(viewsets.ModelViewSet):
    serializer_class = CollaboratorSerializer
    def get_queryset(self):
        return Collaborator.objects.select_related('user').filter(user__is_superuser=False)