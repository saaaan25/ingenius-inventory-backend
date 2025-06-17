from rest_framework.views import APIView
from rest_framework.response import Response
from ..queries import (
    get_request_statistics, get_plan_request_statistics,
    get_requested_utils, get_plan_requested_utils,
    get_general_statistics, get_plan_general_statistics,
    get_purchase_statistics, get_plan_purchase_statistics,
    get_utils_by_teacher, get_plan_utils_by_teacher
)


# Estadísticas de solicitudes

class RequestStatisticsView(APIView):
    def get(self, request):
        result = get_request_statistics()
        data = {
            "total": result[0],
            "accepted": result[1],
            "rejected": result[2],
            "completed": result[3],
            "acceptance_percentage": result[4]
        }
        return Response(data)

class PlanRequestStatisticsView(APIView):
    def get(self, request):
        plan = get_plan_request_statistics()
        return Response({"plan": plan})


# Útiles de solicitudes 

class RequestedUtilsView(APIView):
    def get(self, request):
        result = get_requested_utils()
        data = {
            "total_requested": result[0], 
            "accepted_requested": result[1]
        }
        return Response(data)

class PlanRequestedUtilsView(APIView):
    def get(self, request):
        plan = get_plan_requested_utils()
        return Response({"plan": plan})


# Estadísticas generales

class GeneralStatisticsView(APIView):
    def get(self, request):
        result = get_general_statistics()
        data = {
            "utiles_disponibles": result[0],
            "dinero_disponible": float(result[1]) if result[1] is not None else 0.0
        }
        return Response(data)

class PlanGeneralStatisticsView(APIView):
    def get(self, request):
        plan = get_plan_general_statistics()
        return Response({"plan": plan})


# Estadísticas de compras

class PurchaseStatisticsView(APIView):
    def get(self, request):
        result = get_purchase_statistics()
        data = {
            "total_purchases": result[0], 
            "total_utils": result[1], 
            "total_spent": result[2]
        }
        return Response(data)

class PlanPurchaseStatisticsView(APIView):
    def get(self, request):
        plan = get_plan_purchase_statistics()
        return Response({"plan": plan})


# Útiles por profesor

class UtilsByTeacherView(APIView):
    def get(self, request):
        user_id = request.query_params.get('user_id')
        try:
            user_id = int(user_id) if user_id else None
        except ValueError:
            return Response({"error": "El parámetro 'user_id' debe ser un entero."}, status=400)

        results = get_utils_by_teacher(user_id)
        data = [{"description": r[0], "quantity": r[1]} for r in results]
        return Response(data)


class PlanUtilsByTeacherView(APIView):
    def get(self, request):
        user_id = request.query_params.get("user_id")
        try:
            user_id = int(user_id) if user_id else None
        except ValueError:
            return Response({"error": "El parámetro 'user_id' debe ser un entero válido."}, status=400)
        plan = get_plan_utils_by_teacher(user_id)
        return Response({"plan": plan})