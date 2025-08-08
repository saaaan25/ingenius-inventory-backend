from django.urls import path
from .views import (
    Classrooms, ClassroomDetail,
    Deliveries, DeliveryDetail, 
)

urlpatterns = [
    path('classrooms/', Classrooms.as_view()),
    path('classrooms/<int:pk>/', ClassroomDetail.as_view()), 
    path('deliveries/', Deliveries.as_view()),
    path('deliveries/<int:pk>/', DeliveryDetail.as_view()),
]