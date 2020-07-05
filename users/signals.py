from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def save_or_create_profile_for_existing_user(sender, instance, created, *args, **kwargs):
    try:
        if created:
            instance.profile.save()
    except Profile.DoesNotExist:
        Profile.objects.create(user=instance)

    # if created:
    #     Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()
