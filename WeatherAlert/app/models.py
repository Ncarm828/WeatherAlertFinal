"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UsersProfile (models.Model):

    username = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    phoneNumber = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=10, blank=True)
    time = models.CharField(max_length=10, blank=True)
    acknowledgment = models.BooleanField(default=True)
    userVerificationCode = models.CharField(max_length=20, blank=True)
    generatedVerificationCode = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return str(self.username)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UsersProfile.objects.create(username=kwargs['instance'])

post_save.connect(create_profile, sender=User)
