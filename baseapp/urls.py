from django.urls import path
from . import views

app_name = "baseapp"


urlpatterns = [
    path('', views.homePage, name="homepage"),
    path('admin-panel/', views.adminPanel, name="admin-panel"),
]
