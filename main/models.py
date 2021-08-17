import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import utc
from django.utils.translation import gettext_lazy as _


class Team(models.Model):
    """
    Model for the data related to each team participated in the league
    """

    name = models.CharField(max_length=40)
    average_score = models.DecimalField(default=0, decimal_places=2, max_digits=5)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('team')
        verbose_name_plural = _('teams')

    def belongs_to(self, coach):
        """
        Check particular team is coached by given coach user

        Args:
            coach (User): A lazy user instance of an authenticated coach user

        Returns:
            boolean: True if team coach is equal to given coach user; else False
        """
        return self.coach.email == coach.email


class User(AbstractUser):
    """
    Extended User model from Django Auth module to define a custom User model for the application
    """

    ADMIN = 1
    COACH = 2
    PLAYER = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (COACH, 'Coach'),
        (PLAYER, 'Player')
    )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=False, null=False, default=3)
    login_count = models.IntegerField(default=0)
    time_spent = models.FloatField(default=0)
    online = models.BooleanField(default=False)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def record_login(self):
        """
        Updates the login related statuses upon user login
        """
        self.login_count += 1
        self.online = True
        self.save()

    def record_logout(self):
        """
        Updates the login related statuses upon user logout
        """
        self.online = False
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        time_difference = now - self.last_login
        self.time_spent += time_difference.total_seconds()
        self.save()


class Admin(User):
    """
    Extended model for Admin user from custom User model
    """

    def __str__(self):
        return self.first_name


class Coach(User):
    """
    Extended model for Coach user from custom User model
    """

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
    """
    Extended model for Player user from custom User model
    """

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
        """
        Check particular player's team coached by given coach user

        Args:
            coach (User): A lazy user instance of an authenticated coach user

        Returns:
            boolean: True if player's team coach is equal to given coach user; else False
        """
        return self.team.coach.email == coach.email


class Match(models.Model):
    """
    Model for the data related to each match played in the league
    """

    round = models.IntegerField(null=False, blank=False)
    team_a_score = models.IntegerField(null=False, blank=False)
    team_b_score = models.IntegerField(null=False, blank=False)
    team_a = models.ForeignKey(
        Team,
        related_name="team_a",
        on_delete=models.CASCADE
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

    def __str__(self):
        return self.name

    @property
    def name(self):
        """
        Name property derived from other details of the match

        Returns:
            string: containing both team names and respective scores as a label
        """
        return "{}-({}) vs {}-({})".format(self.team_a.name, self.team_a_score, self.team_b.name, self.team_b_score)

    class Meta:
        verbose_name = _('match')
        verbose_name_plural = _('matches')
