from django.urls import path
from . import views

app_name = "baseapp"


urlpatterns = [
    path('', views.index, name='index'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    path('my-profile-tab', views.myProfileTab, name='my-profile-tab'),
    path('guilds-tab/', views.guildsTab, name='guilds-tab'),
    path('challenges-tab/', views.challengesTab, name='challenges-tab'),
    path('buy-in-tab/', views.buyInTab, name='buy-in-tab'),
    path('my-tickets-tab/', views.myTicketsTab, name='my-tickets-tab'),
    path('battles-tab/', views.battlesTab, name='battles-tab'),
    path('admin-panel/', views.adminPanel, name="admin-panel"),
]
