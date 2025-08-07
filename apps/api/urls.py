from django.urls import path
from .views import classroomsView, deliveriesView

urlpatterns = [
    path('classrooms/', classroomsView),
    path('classrooms/<int:pk>/', classroomDetailView), 
    path('deliveries/', deliveriesView),
    path('deliveries/<int:pk>/', deliveryDetailView),
]