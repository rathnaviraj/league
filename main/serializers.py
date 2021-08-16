from rest_framework import serializers

from main.models import Player, Team, Match


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    """
    Extended HyperlinkedModelSerializer for Player
    """

    class Meta:
        model = Player
        fields = ['url', 'first_name', 'last_name', 'height', 'average_score', 'number_of_games', 'team']


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    """
    Extended HyperlinkedModelSerializer for Team
    """

    class Meta:
        model = Team
        fields = ['url', 'name', 'average_score', 'player_set']


class MatchSerializer(serializers.HyperlinkedModelSerializer):
    """
    Extended HyperlinkedModelSerializer for Match
    """

    class Meta:
        model = Match
        fields = ['url', 'name', 'round', 'team_a', 'team_b', 'winner', 'team_a_qualifying_match',
                  'team_b_qualifying_match']
