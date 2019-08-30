from django.contrib.auth.models import AnonymousUser
from rest_framework import permissions


class OnlyForNonAuthorized(permissions.BasePermission):
    def has_permission(self, request, view):
        return isinstance(request.user, AnonymousUser)
