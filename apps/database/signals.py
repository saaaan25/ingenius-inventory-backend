from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Collaborator

@receiver(post_save, sender=User)
def create_collaborator(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        Collaborator.objects.get_or_create(user=instance)