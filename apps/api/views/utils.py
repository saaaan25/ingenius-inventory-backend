from apps.utils.models import Util
from apps.api.serializers.utils import UtilSerializer
from rest_framework import generics

class Utils(generics.ListCreateAPIView):
    queryset = Util.objects.all()
    serializer_class = UtilSerializer
    search_fields = ['name']
    ordering_fields = ['name', 'quantity']

class UtilDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Util.objects.all()
    serializer_class = UtilSerializer
    lookup_field = 'pk'
