from rest_framework import permissions

from main.models import User


class IsCoachOrAdmin(permissions.BasePermission):
    """
    Role based permission checks
    """

    def has_object_permission(self, request, view, obj):
        authorized = request.user.role == User.ADMIN

        if request.user.role == User.COACH:
            authorized = obj.belongs_to(request.user)

        return authorized


class IsAdmin(permissions.BasePermission):
    """
    Role based permission checks
    """

    def has_permission(self, request, view):
        return request.user.role == User.ADMIN