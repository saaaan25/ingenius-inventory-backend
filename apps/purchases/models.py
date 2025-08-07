from django.db import models
import uuid
from utils.models import *
from django.contrib.auth.models import User

class Purchase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    purchase_date = models.DateField()
    administrator = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(decimal_places=2)

    def __str__(self):
        return f"Compra {self.purchase_date}"


class PurchaseDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    util = models.ForeignKey(Util, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=2)

    def __str__(self):
        return f"{self.util.name} x{self.quantity} - {self.price}"

