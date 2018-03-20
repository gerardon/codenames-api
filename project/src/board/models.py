import random, string
from collections import Counter
from django.db import models
from django.contrib.postgres.fields import ArrayField

from src.constants import WORDS, RED, BLUE, INNOCENT, ASSASSIN, CARD_RESPONSE_CHOICES

class Board(models.Model):
    name = models.CharField(max_length=25)
    invite_code = models.CharField(max_length=25)
    words = ArrayField(models.CharField(max_length=50, blank=True), size=25)
    response_card = ArrayField(models.CharField(choices=CARD_RESPONSE_CHOICES, max_length=20, blank=True), size=25, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.invite_code:
            self.invite_code = ''.join(
                random.choices(string.ascii_lowercase + string.digits, k=25)
            )

        if not self.words:
            self.words = random.sample(WORDS, k=25)

        if not self.response_card:
            self.response_card = self._generate_response_card()

        return super(Board, self).save(*args, **kwargs)

    @property
    def starting_team(self):
        counter = Counter(
            [team for team in self.response_card if team in [RED, BLUE]]
        )
        return counter.most_common()[0][0]

    def _generate_response_card(self):
        choices = [INNOCENT] * 9 + [ASSASSIN]
        starting_team = random.choice([RED, BLUE])
        for team in [RED, BLUE]:
            if team == starting_team:
                choices += [team] * 9
            else:
                choices += [team] * 8

        random.shuffle(choices)

        return choices
