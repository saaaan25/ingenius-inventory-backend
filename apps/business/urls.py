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
from .views.deliveries import (
    UtilsByListView, PlanUtilsByListView,
    StudentsByClassView, PlanStudentsByClassView,
    DeliveriesByStudentView, PlanDeliveriesByStudentView
)
from .views.reports import (
    RequestStatisticsView, PlanRequestStatisticsView,
    RequestedUtilsView, PlanRequestedUtilsView,
    GeneralStatisticsView, PlanGeneralStatisticsView,
    PurchaseStatisticsView, PlanPurchaseStatisticsView,
    UtilsByTeacherView, PlanUtilsByTeacherView
)

urlpatterns = [
    path('users/by-role/', UsersByRoleView.as_view(), name='users-by-role'),
    path('users/by-role/plan/', PlanUsersByRoleView.as_view(), name='plan-users-by-role'),
    path('requests/by-status/', RequestsByStatusView.as_view(), name='requests-by-status'),
    path('requests/by-status/plan/', PlanRequestsByStatusView.as_view(), name='plan-requests-by-status'),
    path('utils/by-request/', UtilsByRequestView.as_view(), name='utils-by-request'),
    path('utils/by-request/plan/', PlanUtilsByRequestView.as_view(), name='plan-utils-by-request'),
    path('purchases/ordered-by-date/', PurchasesOrderedByDateView.as_view(), name='purchases-ordered-by-date'),
    path('purchases/ordered-by-date/plan/', PlanPurchasesOrderedByDateView.as_view(), name='plan-purchases-ordered-by-date'),
    path('utils/by-purchase/', UtilsByPurchaseView.as_view(), name='utils-by-purchase'),
    path('utils/by-purchase/plan/', PlanUtilsByPurchaseView.as_view(), name='plan-utils-by-purchase'),
    path('utils/by-list/', UtilsByListView.as_view(), name='utils-by-list'),
    path('utils/by-list/plan/', PlanUtilsByListView.as_view(), name='plan-utils-by-list'),
    path('students/by-class/', StudentsByClassView.as_view(), name='students-by-class'),
    path('students/by-class/plan/', PlanStudentsByClassView.as_view(), name='plan-students-by-class'),
    path('deliveries/by-student/', DeliveriesByStudentView.as_view(), name='deliveries-by-student'),
    path('deliveries/by-student/plan/', PlanDeliveriesByStudentView.as_view(), name='plan-deliveries-by-student'),
    path('statistics/requests/', RequestStatisticsView.as_view(), name='requests-statistics'),
    path('statistics/requests/plan/', PlanRequestStatisticsView.as_view(), name='plan-requests-statistics'),
    path('statistics/requests/utils/', RequestedUtilsView.as_view(), name='requested-utils-statistics'),
    path('statistics/requests/utils/plan/', PlanRequestedUtilsView.as_view(), name='plan-requested-utils-statistics'),
    path('statistics/', GeneralStatisticsView.as_view(), name='general-statistics'),
    path('statistics/plan/', PlanGeneralStatisticsView.as_view(), name='plan-general-statistics'),
    path('statistics/purchases/', PurchaseStatisticsView.as_view(), name='purchases-statistics'),
    path('statistics/purchases/plan/', PlanPurchaseStatisticsView.as_view(), name='plan/purchases-statistics'),
    path('statistics/utils/by-teacher/', UtilsByTeacherView.as_view(), name='utils-by-teacher'),
    path('statistics/utils/by-teacher/plan/', PlanUtilsByTeacherView.as_view(), name='plan-utils-by-teacher')
]