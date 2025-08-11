from apps.lists.models import List, ListDetail
from apps.api.serializers import ListSerializer, ListDetailSerializer
from rest_framework import generics
from apps.api.filters import ListDetailFilter

class Lists(generics.ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    search_fields = ['classroom__name']
    ordering_fields = ['classroom__name']

class ListDet(generics.RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    lookup_field = 'pk'

class ListDetails(generics.ListCreateAPIView):
    queryset = ListDetail.objects.all()
    serializer_class = ListDetailSerializer
    filterset_class = ListDetailFilter
    search_fields = ['list__name']
    ordering_fields = ['util__name']

class ListDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ListDetail.objects.all()
    serializer_class = ListDetailSerializer
    lookup_field = 'pk'