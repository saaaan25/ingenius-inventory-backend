from rest_framework.views import APIView
from rest_framework.response import Response
from ..queries import get_users_by_role, get_plan_users_by_role

class UsersByRoleView(APIView):
    def get(self, request):
        role = request.query_params.get('role', 'profesor')
        resultados = get_users_by_role(role)
        data = [{"id": r[0], "email": r[1], "name": r[2], "lastname": r[3]} for r in resultados]
        return Response(data)

class PlanUsersByRoleView(APIView):
    def get(self, request):
        role = request.query_params.get('role', 'profesor')
        plan = get_plan_users_by_role(role)
        return Response({"plan": plan})