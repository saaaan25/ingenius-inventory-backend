from django.urls import path
from .views.users import UsersByRoleView, PlanUsersByRoleView

urlpatterns = [
    path('api/users/by-role/', UsersByRoleView.as_view(), name='users-by-role'),
    path('api/plan/users/by-role/', PlanUsersByRoleView.as_view(), name='plan-users-by-role')
]