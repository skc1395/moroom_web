from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=30)

    def __str__(self):
        return self.contact

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Photo(models.Model):
    image = models.ImageField()


class Post(models.Model):
    title = models.CharField(max_length=25)
    images = models.ForeignKey(Photo)

    def __str__(self):
        return self.title
