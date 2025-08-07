from django.db import models
import uuid
from django.contrib.auth.models import User

class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    title = models.CharField(max_length=30)
    message = models.TextField(max_length=500)
    created_at = models.DateField()
    type = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.created_at} - {self.type}"
    

class Addressee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.notification.title} - {self.user.name} {self.user.last_name}"
