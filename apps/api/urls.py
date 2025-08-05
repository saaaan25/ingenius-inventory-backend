from django.urls import path
from . import views

urlpatterns = [
    path('classrooms/', views.classroomsViews)
    path('deliveries/', views.deliveriesViews)
]