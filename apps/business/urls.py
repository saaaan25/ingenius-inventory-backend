from django.urls import path
from .views.users import UsersByRoleView, PlanUsersByRoleView
from .views.requests import (
    RequestsByStatusView, PlanRequestsByStatusView, 
    UtilsByRequestView, PlanUtilsByRequestView
)
from .views.purchases import (
    PurchasesOrderedByDateView, PlanPurchasesOrderedByDateView,
    UtilsByPurchaseView, PlanUtilsByPurchaseView
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
    path('utils/by-request/plan/', PlanUtilsByRequestView.as_view(), name='plan-utils-by-request'),
    path('purchases/ordered-by-date/', PurchasesOrderedByDateView.as_view(), name='purchases-ordered-by-date'),
    path('purchases/ordered-by-date/plan/', PlanPurchasesOrderedByDateView.as_view(), name='plan-purchases-ordered-by-date'),
    path('utils/by-purchase/', UtilsByPurchaseView.as_view(), name='utils-by-purchase'),
    path('utils/by-purchase/plan/', PlanUtilsByPurchaseView.as_view(), name='plan-utils-by-purchase')
]