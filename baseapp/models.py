from django.db import models
from django.contrib.auth.models import AbstractUser


class Genre(models.Model):
    genre_name = models.CharField(max_length=255, blank=True, null=True)
    genre_image = models.ImageField(blank=True, null=True)
    genre_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.genre_name}'


class Rank(models.Model):
    rank_name = models.CharField(max_length=255, blank=True, null=True)
    rank_min_point = models.IntegerField(blank=True, null=True)
    rank_max_point = models.IntegerField(blank=True, null=True)
    rank_color = models.CharField(max_length=50, blank=True, null=True)
    rank_hp_boost = models.IntegerField(blank=True, null=True)
    rank_image = models.FileField(upload_to="rank-image")

    def __str__(self):
        return f'{self.rank_name}'


class Guild(models.Model):
    guild_name = models.CharField(max_length=50)
    guild_image = models.FileField(upload_to="guild-image")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.guild_name}'


class GuildRank(models.Model):
    guild_rank_name = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.guild_rank_name}'


class Battle(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.type}'


class Ticket(models.Model):
    type = models.ForeignKey(
        Battle, on_delete=models.CASCADE, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    sell_back_price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.type}'


class BuyIn(models.Model):
    type = models.ForeignKey(
        Ticket, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.type}'


class User(AbstractUser):
    user_dob = models.DateField(blank=True, null=True)
    user_image = models.ImageField(upload_to="user-image", null=True)
    user_gold = models.IntegerField(blank=True, null=True, default=100)
    user_music = models.CharField(max_length=50, blank=True, null=True)
    user_rank = models.ForeignKey(
        Rank, on_delete=models.CASCADE, blank=True, null=True)
    user_genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE, blank=True, null=True)
    user_guild = models.ForeignKey(
        Guild, on_delete=models.CASCADE, blank=True, null=True)
    user_guild_rank = models.ForeignKey(
        GuildRank, on_delete=models.CASCADE, blank=True, null=True)
    user_xp = models.IntegerField(default=0, blank=True, null=True)
    user_hp = models.IntegerField(default=100, null=True)
    user_max_hp = models.IntegerField(default=100, null=True)
    user_is_profile_completed = models.BooleanField(
        blank=True, null=True, default=False)

    def __str__(self):
        return f'{self.username} - {self.user_genre}'


class GuildLeaderBoard(models.Model):
    guild = models.ForeignKey(
        Guild, on_delete=models.CASCADE, blank=True, null=True)
    guild_rank = models.ForeignKey(
        GuildRank, on_delete=models.CASCADE, blank=True, null=True)
    guild_rank_holder = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.guild} - {self.guild_rank} - {self.guild_rank_holder}'


class UserTicket(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    type = models.ForeignKey(
        Ticket, on_delete=models.CASCADE, blank=True, null=True)
    num_of_tickets = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return f'{self.type}'


class UserBuyIn(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    type = models.ForeignKey(
        BuyIn, on_delete=models.CASCADE, blank=True, null=True)
    num_of_buy_ins = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.type}'
