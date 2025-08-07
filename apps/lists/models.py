from django.db import models
import uuid
from apps.classrooms.models import *
from apps.utils.models import *

class List(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=15)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.classroom.name}"
    

class ListDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    util = models.ForeignKey(Util, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.list.name} - {self.util.name} x{self.quantity}"
