from django.db import models
from django.contrib.auth.models import User
import os


GENDER_CHOICES = ((0, 'female'), (1, 'male'), (2, 'undefined'))


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.IntegerField(choices = GENDER_CHOICES, null=True, blank=True, default=3)
    birth_date = models.DateField(default='1998-9-9',  null=True, blank=True)
    favorites = models.JSONField(default=list, null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()

    def get_mobile(self):
        return self.mobile
    
    def get_favorites(self):
        return self.favorites

    def get_gender(self):
        return self.gender

    def get_birth_date(self):
        return self.birth_date


