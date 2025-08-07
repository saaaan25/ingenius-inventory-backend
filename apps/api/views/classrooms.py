from django.shortcuts import render
from django.http import JsonResponse
from apps.classrooms.models import Classroom, Student

def classroomsView(request):
    classrooms = Classroom.objects.all()
    classrooms_list = list(classrooms.values())
    print(classrooms)
    return JsonResponse(classrooms_list, safe=False)