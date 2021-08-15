from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=40)
    average_score = models.DecimalField(default=0, decimal_places=2, max_digits=5)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('team')
        verbose_name_plural = _('teams')

    def belongs_to(self, coach):
        return self.coach.email == coach.email


class User(AbstractUser):

    ADMIN = 1
    COACH = 2
    PLAYER = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (COACH, 'Coach'),
        (PLAYER, 'Player')
    )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=False, null=False, default=3)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Admin(User):

    def __str__(self):
        return self.first_name


class Coach(User):
    team = models.OneToOneField(
        Team,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return "{} {} - {}".format(self.first_name, self.last_name, self.team.name)

    class Meta:
        verbose_name = _('coach')
        verbose_name_plural = _('coaches')


class Player(User):
    height = models.DecimalField(default=0, decimal_places=2, max_digits=5)
    average_score = models.FloatField(default=0)
    number_of_games = models.IntegerField(default=0)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        verbose_name = _('player')
        verbose_name_plural = _('players')

    def belongs_to(self, coach):
        return self.team.coach.email == coach.email


class Match(models.Model):
    round = models.IntegerField(null=False, blank=False)
    team_a_score = models.IntegerField(null=False, blank=False)
    team_b_score = models.IntegerField(null=False, blank=False)
    team_a = models.ForeignKey(
        Team,
        related_name="team_a",
        on_delete=models.CASCADE,

    )
    team_b = models.ForeignKey(
        Team,
        related_name="team_b",
        on_delete=models.CASCADE
    )
    winner = models.ForeignKey(
        Team,
        related_name="winner",
        on_delete=models.CASCADE
    )
    team_a_qualifying_match = models.OneToOneField(
        'self',
        related_name="a_qualifying_match",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    team_b_qualifying_match = models.OneToOneField(
        'self',
        related_name="b_qualifying_match",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )


    @property
    def name(self):
        return "{}-({}) vs {}-({})".format(self.team_a.name, self.team_a_score, self.team_b.name, self.team_b_score)

    @property
    def a_team(self):
        return {"name": self.team_a.name, "url": self.team_a}

    @property
    def b_team(self):
        return {"name": self.team_b.name, "url": self.team_b}

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('match')
        verbose_name_plural = _('matches')