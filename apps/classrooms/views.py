from django.shortcuts import render
from django.http import HttpResponse

def classrooms(request):
    classrooms = [
        {'id': 1, 'name': '1er grado'}
    ]
    return HttpResponse(classrooms)
