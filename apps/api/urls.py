from django.urls import path
from views import classroomsView, deliveriesView

urlpatterns = [
    path('classrooms/', classroomsView),
    path('deliveries/', deliveriesView),
]