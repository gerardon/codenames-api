from django.urls import path
from src.player import views
urlpatterns = [
    path('', views.player_view),
]
