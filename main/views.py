from rest_framework import permissions
from rest_framework import viewsets

from main import permissions as custom_permissions
from main.models import Player, Team, Match
from main.serializers import PlayerSerializer, TeamSerializer, MatchSerializer


class PlayerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Player.objects.all().order_by('-date_joined')
    serializer_class = PlayerSerializer
    permission_classes = [permissions.IsAuthenticated, custom_permissions.IsCoachOrAdmin]


class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated, custom_permissions.IsCoachOrAdmin]


class MatchViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Match.objects.all().order_by('round')
    serializer_class = MatchSerializer
    permission_classes = [permissions.IsAuthenticated]