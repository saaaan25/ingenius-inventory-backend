from apps.requests.models import Request, RequestDetail
from apps.api.serializers.requests import RequestSerializer, RequestDetailSerializer
from rest_framework import generics

class Requests(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

class RequestDet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    lookup_field = 'pk'

class RequestDetails(generics.ListCreateAPIView):
    queryset = RequestDetail.objects.all()
    serializer_class = RequestDetailSerializer

class RequestDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RequestDetail.objects.all()
    serializer_class = RequestDetailSerializer
    lookup_field = 'pk'
