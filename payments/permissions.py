from rest_framework import permissions


class IsAdminForWrite(permissions.BasePermission):
    """
    Read-only for authenticated users,
    write (POST/PUT/PATCH/DELETE) only for staff / superuser.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)
        return bool(
            request.user and request.user.is_staff and request.user.is_superuser
        )
