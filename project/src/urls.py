from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('board/', include('src.board.urls')),
    path('player/', include('src.player.urls')),
    path('admin/', admin.site.urls),
]
