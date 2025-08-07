from django.urls import path
from views import *

urlpatterns = [
    path('classrooms/', classroomsView),
    path('deliveries/', deliveriesView),
]