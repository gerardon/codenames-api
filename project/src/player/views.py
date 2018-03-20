from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from src.board.authentication import BoardAuthentication, HasBoardPermission
from src.player.serializers import PlayerSerializer

class PlayerCreateView(CreateAPIView):
    serializer_class = PlayerSerializer
    authentication_classes = [BoardAuthentication]
    permission_classes = [HasBoardPermission]

player_view = PlayerCreateView.as_view()
