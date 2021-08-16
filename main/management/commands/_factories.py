import factory

from main.models import Player


class PlayerFactory(factory.Factory):
    """
    Custom factory class for generating Player instances for management commands
    """

    class Meta:
        model = Player

    role = 3
    password = 'pbkdf2_sha256$260000$4IQYXmeJrzp5Ivpmh74yfQ$1GlRMyF8WP8BbDY1IPNGdnyKcDRbQQlMHccWvWRVpWc='
    is_staff = False
    is_active = True
