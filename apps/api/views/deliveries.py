from django.shortcuts import render
from django.http import JsonResponse
from apps.deliveries.models import Delivery, UtilDelivery, MoneyDelivery

def deliveriesView(request):
    deliveries = Delivery.objects.all().values()
    print(deliveries)
    return JsonResponse(list(deliveries), safe=False)

