from django.urls import path
from . import views

# app_name = "baseapp"


urlpatterns = [
    path('', views.index, name='index'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    path('my-profile-tab', views.myProfileTab, name='my-profile-tab'),
    path('guilds-tab/', views.guildsTab, name='guilds-tab'),
    path('user-guild-overview/', views.userGuildOverview, name='user-guild-overview'),
    path('selected-guild/<slug:guild_slug>', views.selectedGuild, name='selected-guild'),
    path('selected-guild/<slug:guild_slug>/<slug:guild_rank_slug>', views.guildRankPlayers, name='guild-rank-players'),
    path('challenges-tab/', views.challengesTab, name='challenges-tab'),
    path('buy-in-tab/', views.buyInTab, name='buy-in-tab'),
    path('my-tickets-tab/', views.myTicketsTab, name='my-tickets-tab'),
    path('battles-tab/', views.battlesTab, name='battles-tab'),
    path('admin-panel/', views.adminPanel, name="admin-panel"),
]
