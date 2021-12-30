from django.db import models
from django.contrib.auth.models import AbstractUser

class Rank(models.Model):
    rank_name = models.CharField(max_length=255, blank=True, null=True)
    rank_min_point = models.IntegerField(blank=True, null=True)
    rank_max_point = models.IntegerField(blank=True, null=True)
    rank_color = models.CharField(max_length=50, blank=True, null=True)
    rank_hp_boost = models.IntegerField(blank=True, null=True)
    rank_image = models.FileField(upload_to="rank-image")

    def __str__(self):
      return f'{self.rank_name} - {self.rank_min_point} - {self.rank_max_point} - {self.rank_color} - {self.rank_hp_boost}'

class Guild(models.Model):
    guild_name = models.CharField(max_length=50)
    guild_image = models.FileField(upload_to="guild-image")

    def __str__(self):
      return f'{self.guild_name}'

class GuildRank(models.Model):
    guild_rank_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
      return f'{self.guild_rank_name}'

class User(AbstractUser):
    user_dob = models.DateField(blank=True, null=True)
    user_image = models.ImageField(upload_to="user-image", null=True)
    user_gold = models.IntegerField(blank=True, null=True)
    user_tickets = models.CharField(max_length=50, blank=True, null=True)
    user_music = models.CharField(max_length=50, blank=True, null=True)
    user_rank = models.ForeignKey(Rank, on_delete=models.CASCADE, blank=True, null=True)
    user_genre = models.CharField(max_length=50, blank=True, null=True)
    user_guild = models.ForeignKey(Guild, on_delete=models.CASCADE, blank=True, null=True)
    user_guild_rank = models.ForeignKey(GuildRank, on_delete=models.CASCADE, blank=True, null=True)
    user_xp = models.IntegerField(blank=True, null=True)
    user_hp = models.IntegerField(default=100, null=True)

    def __str__(self):
      return f'{self.username} - {self.user_genre}'

class GuildLeaderBoard(models.Model):
    guild = models.ForeignKey(Guild, on_delete=models.CASCADE, blank=True, null=True)
    guild_rank = models.ForeignKey(GuildRank, on_delete=models.CASCADE, blank=True, null=True)
    guild_rank_holder = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
      return f'{self.guild} - {self.guild_rank} - {self.guild_rank_holder}'