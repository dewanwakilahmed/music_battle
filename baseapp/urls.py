from django.urls import path
from . import views

# app_name = "baseapp"


urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('new-profile/', views.profileCreation, name='profile-creation'),
    path('my-profile-tab', views.myProfileTab, name='my-profile-tab'),
    path('guilds-tab/', views.guildsTab, name='guilds-tab'),
    path('user-guild-overview/', views.userGuildOverview, name='user-guild-overview'),
    path('selected-guild/<slug:guild_slug>', views.selectedGuild, name='selected-guild'),
    path('selected-guild/<slug:guild_slug>/<slug:guild_rank_slug>', views.guildRankPlayers, name='guild-rank-players'),
    path('challenges-tab/', views.challengesTab, name='challenges-tab'),
    path('buy-in-tab/', views.buyInTab, name='buy-in-tab'),
    path('user-buy-in-overview/', views.userBuyInOverview, name="user-buy-in-overview"),
    path('buy-in-actions/<user_buy_in>', views.buyInActions, name='buy-in-actions'),
    path('my-tickets-tab/', views.myTicketsTab, name='my-tickets-tab'),
    path('user-tickets-overview/', views.userTicketsOverview, name='user-tickets-overview'),
    path('ticket-actions/<selected_ticket>', views.ticketActions, name='ticket-actions'),
    path('buy-tickets/', views.buyTickets, name='buy-tickets'),
    path('battles-tab/', views.battlesTab, name='battles-tab'),
    path('admin-panel/', views.adminPanel, name="admin-panel"),
    path("logout", views.logout_request, name='logout')
]
