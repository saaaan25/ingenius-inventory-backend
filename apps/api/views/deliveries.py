from django.shortcuts import render
from django.http import JsonResponse
from apps.deliveries.models import Delivery, UtilDelivery, MoneyDelivery

def deliveriesView(request):
    deliveries = Delivery.objects.all().values()
    deliveries_list = list(deliveries)
    return JsonResponse(deliveries_list, safe=False)

