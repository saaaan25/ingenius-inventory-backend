from rest_framework.views import APIView
from rest_framework.response import Response
from ..queries import (
    get_utils_by_list, get_plan_utils_by_list,
    get_students_by_class, get_plan_students_by_class,
    get_deliveries_by_student, get_plan_deliveries_by_student
)


# Útiles por lista

class UtilsByListView(APIView):
    def get(self, request):
        list_id = request.query_params.get('utils_list_id')
        if not list_id:
            return Response({"error": "El parámetro 'utils_list_id' es requerido."}, status=400)
        results = get_utils_by_list(list_id)
        data = [{"description": r[0], "quantity": r[1]} for r in results]
        return Response(data)

class PlanUtilsByListView(APIView):
    def get(self, request):
        list_id = request.query_params.get('utils_list_id')
        if not list_id:
            return Response({"error": "El parámetro 'utils_list_id' es requerido."}, status=400)
        plan = get_plan_utils_by_list(list_id)
        return Response({"plan": plan})


# Estudiantes por clase

class StudentsByClassView(APIView):
    def get(self, request):
        classroom_id = request.query_params.get('classroom_id')
        if not classroom_id:
            return Response({"error": "El parámetro 'classroom_id' es requerido."}, status=400)
        results = get_students_by_class(classroom_id)
        data = [{"id": r[0], "name": r[1], "lastname": r[2]} for r in results]
        return Response(data)

class PlanStudentsByClassView(APIView):
    def get(self, request):
        classroom_id = request.query_params.get('classroom_id')
        if not classroom_id:
            return Response({"error": "El parámetro 'classroom_id' es requerido."}, status=400)
        plan = get_plan_students_by_class(classroom_id)
        return Response({"plan": plan})


# Entregas por estudiante

class DeliveriesByStudentView(APIView):
    def get(self, request):
        student_id = request.query_params.get('student_id')
        if not student_id:
            return Response({"error": "El parámetro 'student_id' es requerido."}, status=400)
        data = get_deliveries_by_student(student_id)
        return Response(data)

class PlanDeliveriesByStudentView(APIView):
    def get(self, request):
        student_id = request.query_params.get('student_id')
        if not student_id:
            return Response({"error": "El parámetro 'student_id' es requerido."}, status=400)
        plan = get_plan_deliveries_by_student(student_id)
        return Response({"plan": plan})