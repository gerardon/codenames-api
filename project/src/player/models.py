import random, string
from collections import Counter
from django.db import models
from src.constants import TEAMS, RED, BLUE

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
            most_common = counter.most_common()
            if not most_common or (len(most_common) > 1 and most_common[0][1] == most_common[1][1]):
                self.team = self.board.starting_team
            elif len(most_common) == 1:
                teams = [RED, BLUE]
                teams.remove(most_common[0][0])
                self.team = teams[0]
            else:
                self.team = counter.most_common()[-1][0]

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
