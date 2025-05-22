from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'users', UserView, 'users')
router.register(r'utils', UtilView, 'utils')

urlpatterns = [
    path('', include(router.urls))
]
