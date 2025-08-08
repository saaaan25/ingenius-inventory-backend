from django.contrib import admin
from .models import Delivery, UtilDelivery, MoneyDelivery

admin.site.register(Delivery)
admin.site.register(UtilDelivery)
admin.site.register(MoneyDelivery)

