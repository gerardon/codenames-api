from collections import Counter
from django.db import models
from src.constants import TEAMS

class Player(models.Model):
    name = models.CharField(max_length=50)
    team = models.CharField(max_length=4, choices=TEAMS)
    board = models.ForeignKey('board.Board', on_delete=models.CASCADE)
    is_leader = models.BooleanField(default=False)
    auth_token = models.CharField(max_length=25)

    def save(self, *args, **kwargs):
        if not self.team:
            counter = Counter(
                self.board.player_set.values_list('team', flat=True)
            )
            self.team = counter.most_common()[-1][0]
            if not counter.most_common():
                self.team = self.board.starting_team

            if self.board.player_set.filter(team=self.team).count() == 0:
                self.is_leader = True

        if not self.auth_token:
            self.auth_token = ''.join(
                random.choices(
                    string.ascii_lowercase + string.ascii_uppercase + string.digits,
                    k=25
                )
            )

        return super(Player, self).save(*args, **kwargs)
