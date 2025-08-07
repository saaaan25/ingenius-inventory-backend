from django.db import models
import uuid
from django.contrib.auth.models import User

class Classroom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    color = models.CharField(max_length=7)

    def __str__(self):
        return f"{self.name}"
    

class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.last_name}, {self.name}"