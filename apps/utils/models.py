from django.db import models
import uuid

class Util(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=50)  
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} x{self.quantity}"
    

