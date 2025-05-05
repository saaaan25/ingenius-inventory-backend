from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Util)
admin.site.register(Classroom)
admin.site.register(Purchase)
admin.site.register(Request)
admin.site.register(Student)
admin.site.register(Delivery)
admin.site.register(PurchaseDetail)
admin.site.register(RequestDetail)
admin.site.register(UtilsList)
admin.site.register(ListDetail)
admin.site.register(MoneyDelivery)
admin.site.register(UtilsDelivery)
admin.site.register(UtilsDeliveryDetail)
