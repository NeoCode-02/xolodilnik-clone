from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from users.models import Profession
from users.serializers import ProfessionListSerializer


class ProfessionListAPIView(generics.ListAPIView):
    queryset = Profession.objects.all().order_by("id")
    serializer_class = ProfessionListSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["id", "name"]

class ProfessionRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionListSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"


class ProfessionCreateAPIView(generics.CreateAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionListSerializer
    permission_classes = [IsAuthenticated]


class ProfessionUpdateAPIView(generics.UpdateAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionListSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"


class ProfessionDestroyAPIView(generics.DestroyAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionListSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"
