from django.shortcuts import render
from rest_framework import viewsets
from ..serializer import ClassroomSerializer
from ..models import Classroom

class ClassroomView(viewsets.ModelViewSet):
    serializer_class = ClassroomSerializer
    queryset = Classroom.objects.all()