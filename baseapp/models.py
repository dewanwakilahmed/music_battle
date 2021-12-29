from django.db import models
from django.contrib.auth.models import AbstractUser

class Guild(models.Model):
    guild_name = models.CharField(max_length=50)
    guild_image = models.FileField(upload_to="guild-image")

    def __str__(self):
      return f'{self.guild_name}'

class User(AbstractUser):
    user_dob = models.DateField(blank=True, null=True)
    user_image = models.ImageField(upload_to="user-image", null=True)
    user_gold = models.IntegerField(blank=True, null=True)
    user_tickets = models.CharField(max_length=50, blank=True, null=True)
    user_music = models.CharField(max_length=50, blank=True, null=True)
    user_rank = models.CharField(max_length=50, blank=True, null=True)
    user_genre = models.CharField(max_length=50, blank=True, null=True)
    user_guild = models.ForeignKey(Guild, on_delete=models.CASCADE, blank=True, null=True)
    user_guild_rank = models.CharField(max_length=50, blank=True, null=True)
    user_xp = models.IntegerField(blank=True, null=True)
    user_hp = models.IntegerField(default=100, null=True)

    def __str__(self):
      return f'{self.username} - {self.user_genre} - {self.user_guild}'