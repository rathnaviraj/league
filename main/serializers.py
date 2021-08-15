from rest_framework import serializers

from main.models import User, Player, Team, Match


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ['url', 'first_name', 'last_name' 'height', 'average_score', 'number_of_games', 'team']


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ['url', 'name', 'average_score', 'player_set']


class MatchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Match
        fields = ['url', 'name', 'round', 'team_a', 'team_b', 'winner', 'qualified_match']