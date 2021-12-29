from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_image = models.ImageField(upload_to="user-images", null=True)
    user_genre = models.CharField(max_length=50, blank=True, null=True)
    user_guild = models.CharField(max_length=50, blank=True, null=True)
    user_gold = models.IntegerField(blank=True, null=True)
    user_xp = models.IntegerField(blank=True, null=True)
    user_hp = models.IntegerField(default=100, null=True)

