from django.urls import path
from src.board import views
urlpatterns = [
    path('', views.board_view),
]
