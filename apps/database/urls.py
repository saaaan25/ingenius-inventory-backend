from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'users', CollaboratorView, 'users')
router.register(r'utils', UtilView, 'utils')
router.register(r'classrooms', ClassroomView, 'classrooms')
router.register(r'purchases', PurchaseView, 'purchases')
router.register(r'requests', RequestView, 'requests')
router.register(r'students', StudentView, 'students')
router.register(r'deliveries', DeliveryView, 'deliveries')
router.register(r'purchase-details', PurchaseDetailView, 'purchase-details')
router.register(r'request-details', RequestDetailView, 'request-details')
router.register(r'utils-lists', UtilsListView, 'utils-lists')
router.register(r'list-details', ListDetailView, 'list-details')
router.register(r'money-deliveries', MoneyDeliveryView, 'money-deliveries')
router.register(r'utils-deliveries', UtilsDeliveryView, 'utils-deliveries')
router.register(r'utils-delivery-details', UtilsDeliveryDetailView, 'utils-delivery-details')

urlpatterns = [
    path('', include(router.urls))
]
