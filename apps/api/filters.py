import django_filters
from apps.classrooms.models import Student
from apps.deliveries.models import Delivery, UtilDelivery, MoneyDelivery
from apps.lists.models import ListDetail
from apps.notifications.models import Notification, Addressee
from apps.purchases.models import Purchase, PurchaseDetail
from apps.requests.models import Request, RequestDetail
from apps.users.models import Profile

class StudentFilter(django_filters.FilterSet):
    classroom__name = django_filters.CharFilter(field_name='classroom__name', lookup_expr='iexact')
    class Meta:
        model = Student
        fields = ['classroom', 'classroom__name']

class DeliveryFilter(django_filters.FilterSet):
    type = django_filters.CharFilter(field_name='type', lookup_expr='iexact')
    status = django_filters.CharFilter(field_name='status', lookup_expr='iexact')
    class Meta:
        model = Delivery
        fields = ['type', 'status']

class UtilDeliveryFilter(django_filters.FilterSet):
    delivery__student = django_filters.UUIDFilter(field_name='delivery__student__id', lookup_expr='exact')
    delivery__student__last_name = django_filters.CharFilter(field_name='delivery__student__last_name', lookup_expr='exact')
    class Meta:
        model = UtilDelivery
        fields = ['delivery', 'delivery__student', 'delivery__student__last_name']

class MoneyDeliveryFilter(django_filters.FilterSet):
    delivery__student = django_filters.UUIDFilter(field_name='delivery__student__id', lookup_expr='exact')
    delivery__student__last_name = django_filters.CharFilter(field_name='delivery__student__last_name', lookup_expr='exact')
    class Meta:
        model = MoneyDelivery
        fields = ['delivery', 'delivery__student', 'delivery__student__last_name']

class ListDetailFilter(django_filters.FilterSet):
    list__classroom = django_filters.UUIDFilter(field_name='list__classroom__id', lookup_expr='exact')
    list__classroom__name = django_filters.CharFilter(field_name='list__classroom__name', lookup_expr='iexact')
    class Meta:
        model = ListDetail
        fields = ['list', 'list__classroom', 'list__classroom__name']

class NotificationFilter(django_filters.FilterSet):
    type = django_filters.CharFilter(field_name='type', lookup_expr='iexact')
    class Meta:
        model = Notification
        fields = ['type']

class AddresseeFilter(django_filters.FilterSet):
    user__username = django_filters.CharFilter(field_name='user__username', lookup_expr='iexact')
    class Meta:
        model = Addressee
        fields = ['notification', 'user', 'user__username']

class PurchaseFilter(django_filters.FilterSet):
    administrator__username = django_filters.CharFilter(field_name='administrator__username', lookup_expr='iexact')
    class Meta:
        model = Purchase
        fields = ['administrator', 'administrator__username']

class PurchaseDetailFilter(django_filters.FilterSet):
    util__name = django_filters.CharFilter(field_name='util__name', lookup_expr='iexact')
    class Meta:
        model = PurchaseDetail
        fields = ['util', 'util__name', 'purchase']

class RequestFilter(django_filters.FilterSet):
    teacher__username = django_filters.CharFilter(field_name='teacher__username', lookup_expr='iexact')
    status = django_filters.CharFilter(field_name='status', lookup_expr='iexact')
    class Meta:
        model = Request
        fields = ['teacher', 'teacher__username', 'status']

class RequestDetailFilter(django_filters.FilterSet):
    util__name = django_filters.CharFilter(field_name='util__name', lookup_expr='iexact')
    class Meta:
        model = RequestDetail
        fields = ['util', 'util__name', 'request']

class ProfileFilter(django_filters.FilterSet):
    role__name = django_filters.CharFilter(field_name='role__name', lookup_expr='iexact')
    class Meta:
        model = Profile
        fields = ['user', 'role', 'role__name']
