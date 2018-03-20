from rest_framework import serializers
from src.board.models import Board

class BoardSerializer(serializers.ModelSerializer):
    invite_code = serializers.CharField(read_only=True)
    response_card = serializers.SerializerMethodField()

    class Meta:
        model = Board
        fields = [
            'name', 'invite_code', 'words',
            'starting_team', 'response_card'
        ]

    def get_response_card(self, response_card):
        if getattr(self.context['request'].user, 'is_leader', False):
            return obj.response_card

