import random

from django.core.management.base import BaseCommand
from faker import Faker

from main.management.commands._factories import PlayerFactory
from main.models import Team


class Command(BaseCommand):
    """
    Custom management command to generate Players for each team. Not the recommended way of generating player data.
    Check fixtures instead
    """

    help = 'Generates players for each team.'

    def handle(self, *args, **options):
        fake = Faker('en_US')
        teams = Team.objects.all()
        for team in teams:
            for _ in range(10):
                first_name = fake.first_name_male()
                last_name = fake.last_name_male()
                username = '{}.{}'.format(first_name.lower(), last_name.lower())
                email = "%s@example.com" % username
                p = PlayerFactory.create(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    team=team,
                    height=random.randint(160, 210),
                    average_score=random.randint(20, 90),
                    number_of_games=random.randint(0, 15)
                )
                p.save()
