from django.urls import path
from . import views

urlpatterns = [
    path('classrooms/', views.classroomsView),
    path('deliveries/', views.deliveriesView),
]