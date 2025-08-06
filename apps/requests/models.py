from django.db import models
from utils.models import *
import uuid

class Request(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    teacher = models.CharField(max_length=50)  # FK to Teacher
    request_date = models.DateField()
    subject = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Mua mua muaaaaaaaaa"
    

class RequestDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)  # FK to Request
    util = models.ForeignKey(Util, on_delete=models.CASCADE)  # FK to Util
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"I am vaqueishon"