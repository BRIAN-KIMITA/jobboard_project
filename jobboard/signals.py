# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from gunicorn.config import User

from .models import Employer, JobSeeker


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        JobSeeker.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.jobseeker.save()
