from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserDetailSerializer


class UserDetailAPIView(APIView):
    serializer_class = UserDetailSerializer

    def get(self, request, *args, **kwargs):
        print(">>>", args, kwargs, request.user)
        pk = kwargs.get("pk")
        user = self.get_object(pk)
        serializer = self.serializer_class(user)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def get_object(self, pk):
        return User.objects.filter(pk=pk).first()


class UserProfileAPIView(APIView):
    serializer_class = UserDetailSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
