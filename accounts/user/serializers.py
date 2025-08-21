from rest_framework import serializers

from accounts.user.models import User
from accounts.abstract.serializers import AbstractSerializer


class UserSerializer(AbstractSerializer):
    id = serializers.IntegerField(read_only=True)
    public_id = serializers.UUIDField(read_only=True, format="hex")

    class Meta:
        model = User
        fields = [
            "id",
            "public_id",
            "username",
            "name",
            "email",
            "avatar",
            "date_of_birth",
            "theme",
            "is_active",
            "created",
            "updated",
        ]
        read_only_fields = ["is_active", "created", "updated", "public_id", "id"]
