from django.shortcuts import render
from django.http import JsonResponse
from apps.classrooms.models import Classroom, Student

def classroomsView(request):
    classrooms = Classroom.objects.all()
    print(classrooms)
    return JsonResponse(classrooms, safe=False)