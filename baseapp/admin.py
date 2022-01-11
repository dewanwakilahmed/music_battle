from django.contrib import admin

from .models import Rank, User, Guild, GuildRank, GuildLeaderBoard, Genre, Battle, Ticket, BuyIn, UserTicket, UserBuyIn

# Register your models here.

admin.site.register(User)
admin.site.register(Guild)
admin.site.register(GuildRank)
admin.site.register(GuildLeaderBoard)
admin.site.register(Rank)
admin.site.register(Genre)
admin.site.register(Battle)
admin.site.register(Ticket)
admin.site.register(BuyIn)
admin.site.register(UserTicket)
admin.site.register(UserBuyIn)
