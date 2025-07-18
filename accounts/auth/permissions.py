from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(
            f"Object permission check for user: {request.user}, authenticated: {request}"
        )

        if request.user.is_anonymous:
            return request.method in SAFE_METHODS
        return False

    def has_permission(self, request, view):
        print(f"Permission check for user: {request.user}, authenticated: {request}")
        return bool(request.user and request.user.is_authenticated)

        return False
