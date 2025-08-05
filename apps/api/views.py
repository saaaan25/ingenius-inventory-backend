from django.shortcuts import render
from django.http import JsonResponse

def deliveriesView(request):
    deliveries = [
        {'id': 1, 'fecha': '2023-01-01'},
        {'id': 2, 'fecha': '2023-01-02'},
        {'id': 3, 'fecha': '2023-01-03'},
    ] 
    return JsonResponse(deliveries)
