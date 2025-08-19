from rest_framework import serializers

from users.models import User

# class UserListSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     email = serializers.EmailField(read_only=True, max_length=20)
#     first_name = serializers.CharField(read_only=True)
#     last_name = serializers.CharField(read_only=True)
#     phone_number = serializers.CharField(read_only=True)
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "created_at",
            "updated_at",
        ]
