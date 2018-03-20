from rest_framework import serializers
from src.player.models import Player

class PlayerSerializer(serializers.ModelSerializer):
    board = serializers.HiddenField(default=serializers.CurrentUserDefault())
    team = serializers.CharField(read_only=True)
    auth_token = serializers.CharField(read_only=True)

    class Meta:
        model = Player
        fields = ['name', 'board', 'is_leader', 'team', 'auth_token']
