from django.db import models
import uuid

class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    title = models.CharField(max_length=30)
    message = models.TextField(max_length=500)
    created_at = models.DateField()
    type = models.CharField(max_length=20)

    def __str__(self):
        return f"Soy tu pardote osote"
    

class Addressee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)  # FK to Notification
    user = models.CharField(max_length=50) # FK to User

    def __str__(self):
        return f"Teamopandita"
