from apps.requests.models import Request, RequestDetail
from apps.api.serializers.requests import RequestSerializer, RequestDetailSerializer
from rest_framework import generics
from apps.api.filters import RequestFilter, RequestDetailFilter

class Requests(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    filterset_class = RequestFilter

class RequestDet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    lookup_field = 'pk'

class RequestDetails(generics.ListCreateAPIView):
    queryset = RequestDetail.objects.all()
    serializer_class = RequestDetailSerializer
    filterset_class = RequestDetailFilter

class RequestDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RequestDetail.objects.all()
    serializer_class = RequestDetailSerializer
    lookup_field = 'pk'
