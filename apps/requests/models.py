from django.db import models
from apps.utils.models import *
import uuid
from django.contrib.auth.models import User

class Request(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    request_date = models.DateField()
    subject = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.subject} ({self.request_date})"
    

class RequestDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    util = models.ForeignKey(Util, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.request.subject} - {self.util.name} x{self.quantity}"