from django.urls import path
from .views.users import UsersByRoleView, PlanUsersByRoleView
from .views.requests import (
    RequestsByStatusView, PlanRequestsByStatusView, 
    UtilsByRequestView, PlanUtilsByRequestView
)
from django.http import JsonResponse

def prueba_basica(request):
    return JsonResponse({"ok": True})

urlpatterns = [
    path('test/', prueba_basica),
    path('users/by-role/', UsersByRoleView.as_view(), name='users-by-role'),
    path('users/by-role/plan/', PlanUsersByRoleView.as_view(), name='plan-users-by-role'),
    path('requests/by-status/', RequestsByStatusView.as_view(), name='requests-by-status'),
    path('requests/by-status/plan/', PlanRequestsByStatusView.as_view(), name='plan-requests-by-status'),
    path('utils/by-request/', UtilsByRequestView.as_view(), name='utils-by-request'),
    path('utils/by-request/plan/', PlanUtilsByRequestView.as_view(), name='plan-utils-by-request')
]