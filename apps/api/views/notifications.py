from apps.notifications.models import Notification, Addressee
from apps.api.serializers.notifications import NotificationSerializer, AdresseeSerializer
from rest_framework import generics
from apps.api.filters import NotificationFilter, AddresseeFilter

class Notifications(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    filterset_class = NotificationFilter

class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    lookup_field = 'pk'

class Adressees(generics.ListCreateAPIView):
    queryset = Addressee.objects.all()
    serializer_class = AdresseeSerializer
    filterset_class = AddresseeFilter

class AdresseeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Addressee.objects.all()
    serializer_class = AdresseeSerializer
    lookup_field = 'pk'