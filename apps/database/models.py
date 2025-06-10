''' POSTGRESQL '''

from django.db import models
import uuid
from django.contrib.auth.models import User, Group


# Clases

class Collaborator(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Util(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    description = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.description


# Clases con FK (1)

class Classroom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Purchase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_spent = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField()

    def __str__(self):
        return f"Compra {self.purchase_date}"

class Request(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    request_date = models.DateField()
    justification = models.TextField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"Solicitud {self.request_date}"

class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.lastname}"


# Clases con FK (2)

class Delivery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Entrega de {self.student.name}"

class PurchaseDetail(models.Model): # no continúa
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    util = models.ForeignKey(Util, on_delete=models.CASCADE)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.util.description} x{self.quantity} - Compra {self.purchase.purchase_date}"

class RequestDetail(models.Model): # no continúa
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    util = models.ForeignKey(Util, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.util.description} x{self.quantity} - Solicitud {self.request.request_date}"

class UtilsList(models.Model): 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=40)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Lista de útiles de {self.classroom.name} - {self.name}"


# Clases con FK (3)

class ListDetail(models.Model): # no continúa
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    utils_list = models.ForeignKey(UtilsList, on_delete=models.CASCADE)
    util = models.ForeignKey(Util, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.util.description} x{self.quantity} - {self.utils_list.name}"

class MoneyDelivery(models.Model): # no continúa
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    delivery_date = models.DateField(auto_now_add=True)
    observations = models.TextField()

    def __str__(self):
        return f"Monto S/.{self.amount} - {self.delivery.student.name}"

class UtilsDelivery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_date = models.DateField(auto_now_add=True)
    observations = models.TextField()

    def __str__(self):
        return f"Entrega útiles - {self.delivery.student.name}"

# Clases con FK (4)

class UtilsDeliveryDetail(models.Model): # no continúa
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    utils_delivery = models.ForeignKey(UtilsDelivery, on_delete=models.CASCADE)
    util = models.ForeignKey(Util, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"Útil {self.util.description} x{self.quantity} - {self.utils_delivery.delivery.student.name}"



''' MONGODB '''

import mongoengine as me
from mongoengine import DateTimeField, StringField, IntField, FloatField
from datetime import datetime, timezone

class UtilMovement(me.Document):
    MOVEMENT_TYPES = ('Entrada', 'Salida') 

    util = StringField()
    movement_type = StringField(choices=MOVEMENT_TYPES, required=True)
    quantity = IntField(required=True, min_value=1)
    reason = StringField() 
    responsible = StringField()
    timestamp = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def __str__(self):
        return f"{self.movement_type}: {self.util} x{self.quantity} el {self.timestamp} ({self.reason})"

class MoneyMovement(me.Document):
    MOVEMENT_TYPES = ('Entrada', 'Salida')  

    movement_type = StringField(choices=MOVEMENT_TYPES, required=True)
    amount = FloatField(required=True, min_value=0.01)
    reason = StringField() 
    responsible = StringField() 
    timestamp = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def __str__(self):
        return f"{self.movement_type}: S/.{self.quantity} el {self.timestamp} ({self.reason})"