from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import UserProfile
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print("\033[38;5;46m[REGISTER] Utente e profilo One-to-One creati")