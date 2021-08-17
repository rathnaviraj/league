from rest_framework import serializers

from main.models import Player, Coach, Team, Match, User


class StatisticSerializer(serializers.ModelSerializer):
    """
    Extended ModelSerializer for User Statistics
    """

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'login_count', 'online', 'time_spent']


class CoachSerializer(serializers.ModelSerializer):
    """
    Extended ModelSerializer for User Statistics
    """

    class Meta:
        model = Coach
        fields = ['username', 'first_name', 'last_name', 'email']


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    """
    Extended HyperlinkedModelSerializer for Player
    """

    class Meta:
        model = Player
        fields = ['url', 'first_name', 'last_name', 'username', 'height', 'average_score', 'number_of_games', 'team']


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    """
    Extended HyperlinkedModelSerializer for Team
    """

    coach = serializers.SerializerMethodField('get_coach')

    @staticmethod
    def get_coach(obj):
        return CoachSerializer(obj.coach).data

    class Meta:
        model = Team
        fields = ['url', 'name', 'coach', 'average_score', 'player_set']


class MatchSerializer(serializers.HyperlinkedModelSerializer):
    """
    Extended HyperlinkedModelSerializer for Match
    """

    class Meta:
        model = Match
        fields = ['url', 'name', 'round', 'team_a', 'team_b', 'winner', 'team_a_qualifying_match',
                  'team_b_qualifying_match']
