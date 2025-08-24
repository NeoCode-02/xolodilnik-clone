from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserListSerializer
from django_filters.rest_framework import DjangoFilterBackend

class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all().order_by("id")
    serializer_class = UserListSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["profession","is_active"]