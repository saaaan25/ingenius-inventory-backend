from rest_framework.views import APIView
from rest_framework.response import Response
from ..queries import (
    get_purchases_ordered_by_date, get_plan_purchases_ordered_by_date,
    get_utils_by_purchase, get_plan_utils_by_purchase
)

# Compras ordenadas por fecha

class PurchasesOrderedByDateView(APIView):
    def get(self, request):
        results = get_purchases_ordered_by_date()
        data = [{"id": r[0], "date": r[1], "name": r[2], "lastname": r[3], "spent": r[4]} for r in results]
        return Response(data)

class PlanPurchasesOrderedByDateView(APIView):
    def get(self, request):
        plan = get_plan_purchases_ordered_by_date()
        return Response({"plan": plan})


# Útiles por compra

class UtilsByPurchaseView(APIView):
    def get(self, request):
        purchase_id = request.query_params.get('purchase_id')
        if not purchase_id:
            return Response({"error": "El parámetro 'purchase_id' es requerido."}, status=400)
        results = get_utils_by_purchase(purchase_id)
        data = [{"description": r[0], "price": r[1], "quantity": r[2]} for r in results]
        return Response(data)

class PlanUtilsByPurchaseView(APIView):
    def get(self, request):
        purchase_id = request.query_params.get('purchase_id')
        if not purchase_id:
            return Response({"error": "El parámetro 'purchase_id' es requerido."}, status=400)
        plan = get_plan_utils_by_purchase(purchase_id)
        return Response({"plan": plan})