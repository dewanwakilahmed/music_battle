from django.contrib import admin

from .models import Rank, User, Guild, GuildRank, GuildLeaderBoard, Genre

# Register your models here.

admin.site.register(User)
admin.site.register(Guild)
admin.site.register(GuildRank)
admin.site.register(GuildLeaderBoard)
admin.site.register(Rank)
admin.site.register(Genre)
