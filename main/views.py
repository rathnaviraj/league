import numpy as np
from rest_framework import permissions, authentication
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from main import permissions as custom_permissions
from main.models import Player, Team, Match, User
from main.serializers import PlayerSerializer, TeamSerializer, MatchSerializer, StatisticSerializer


class PlayerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be view or list players.
    """
    queryset = Player.objects.all().order_by('average_score')
    serializer_class = PlayerSerializer
    permission_classes = [permissions.IsAuthenticated, custom_permissions.IsCoachOrAdmin]


class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be view or list the team details and filter players.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated, custom_permissions.IsCoachOrAdmin]

    @action(detail=True, renderer_classes=[renderers.JSONRenderer])
    def players(self, request, *args, **kwargs):
        """
        Custom action on TeamViewSet to filter based on a percentile of players average score in a team

        Query Params:
            percentile (int): optional integer value between 0-100.
            if query param isn't provided 90 is considered as default value.

        Returns:
            list: A list of players who has greater than or equal average scores of given percentile value in the
            average score distribution.
        """
        percentile = request.query_params.get('percentile', '90')

        team = self.get_object()
        score_list = list(team.player_set.values_list('average_score', flat=True))
        percentile_value = np.percentile(score_list, int(percentile) if percentile.isnumeric() else 90)
        serializer = PlayerSerializer(
            list(team.player_set.filter(average_score__gte=percentile_value)),
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)


class MatchViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be view or list the details of the matches.
    """
    queryset = Match.objects.all().order_by('round')
    serializer_class = MatchSerializer
    permission_classes = [permissions.IsAuthenticated]


class ListStatistics(APIView):
    """
    View to list all users in the system.

    * Requires basic authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [custom_permissions.IsAdmin]

    def get(self, request):
        """
        Return a list of all users.
        """
        serializer = StatisticSerializer(
            list(User.objects.all()),
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)
