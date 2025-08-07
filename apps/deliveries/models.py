from django.db import models
import uuid
from classrooms.models import *
from lists.models import *

class Delivery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Entrega de {self.student.name} {self.student.last_name} ({self.type})"


class UtilDelivery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    list_detail = models.ForeignKey(ListDetail, on_delete=models.CASCADE)
    delivery_date = models.DateField()

    def __str__(self):
        return f"{self.list_detail.util.name} x{self.list_detail.quantity} - {self.delivery.student.last_name}"


class MoneyDelivery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_date = models.DateField()

    def __str__(self):
        return f"S/.{self.amount} - {self.delivery.student.last_name}"