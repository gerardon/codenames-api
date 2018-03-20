from rest_framework.generics import CreateAPIView
from src.board.serializers import BoardSerializer

class BoardCreateView(CreateAPIView):
    serializer_class = BoardSerializer

board_view = BoardCreateView.as_view()
