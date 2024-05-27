from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save,sender=User)
# ye profile ko create krne ke liye hai
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance) #ye line user ke credential use krke profile create krne mein help kregi


@receiver(post_save,sender=User)
# toh ye profile ko save krne ke liye hai
def save_profile(sender,instance,**kwargs):
    instance.profile.save()