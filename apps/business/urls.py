from django.urls import path
from .views.users import UsersByRoleView, PlanUsersByRoleView

urlpatterns = [
    path('users/by-role/', UsersByRoleView.as_view(), name='users-by-role'),
    path('users/by-role/plan/', PlanUsersByRoleView.as_view(), name='plan-users-by-role')
]