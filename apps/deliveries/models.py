from django.db import models
import uuid

class Delivery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    student = models.CharField(max_length=100)  # FK to Student
    type = models.CharField(max_length=20)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Hola osita quiero que sepas que te amo mucho"


class UtilDelivery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)     # FK to Delivery
    list_detail = models.CharField(max_length=100)  # FK to ListDetail
    delivery_date = models.DateField()

    def __str__(self):
        return f"Perdón si a veces te doy ansiedad mi osita"


class MoneyDelivery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)  # FK to Delivery
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_date = models.DateField()

    def __str__(self):
        return f"Eres y siempre serás mi osita, te amo mucho"