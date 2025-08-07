# from django.shortcuts import render
# from django.http import JsonResponse
from apps.deliveries.models import Delivery, UtilDelivery, MoneyDelivery
from apps.api.serializers.deliveries import DeliverySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def deliveriesView(request):
    if request.method == 'GET':
        deliveries = Delivery.objects.all()
        serializer = DeliverySerializer(deliveries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = DeliverySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

