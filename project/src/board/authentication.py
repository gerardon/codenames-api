from rest_framework.authentication import TokenAuthentication, get_authorization_header
from rest_framework.permissions import BasePermission
from src.board.models import Board


class BoardAuthentication(TokenAuthentication):
    keyword = 'Board'
    model = Board

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            board = model.objects.get(invite_code=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        return (board, None)

class HasBoardPermission(BasePermission):
    def has_permission(self, request, view):
        return isinstance(request.user, Board)
