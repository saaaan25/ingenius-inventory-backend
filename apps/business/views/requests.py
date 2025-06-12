from rest_framework.views import APIView
from rest_framework.response import Response
from ..queries import (
    get_requests_by_status, get_plan_requests_by_status,
    get_utils_by_request, get_plan_utils_by_request
)


# Solicitudes por estatus

class RequestsByStatusView(APIView):
    def get(self, request):
        status = request.query_params.get('status')
        if not status:
            return Response({"error": "El parámetro 'status' es requerido."}, status=400)
        results = get_requests_by_status(status)
        data = [{"id": r[0], "date": r[1], "status": r[2], "name": r[3], "lastname": r[4]} for r in results]
        return Response(data)

class PlanRequestsByStatusView(APIView):
    def get(self, request):
        status = request.query_params.get('status')
        if not status:
            return Response({"error": "El parámetro 'status' es requerido."}, status=400)
        plan = get_plan_requests_by_status(status)
        return Response({"plan": plan})


# Útiles por solicitud

class UtilsByRequestView(APIView):
    def get(self, request):
        request_id = request.query_params.get('request_id')
        if not request_id:
            return Response({"error": "El parámetro 'request_id' es requerido."}, status=400)
        results = get_utils_by_request(request_id)
        data = [{"description": r[0], "quantity": r[1]} for r in results]
        return Response(data)

class PlanUtilsByRequestView(APIView):
    def get(self, request):
        request_id = request.query_params.get('request_id')
        if not request_id:
            return Response({"error": "El parámetro 'request_id' es requerido."}, status=400)
        plan = get_utils_by_request(request_id)
        return Response({"plan": plan})