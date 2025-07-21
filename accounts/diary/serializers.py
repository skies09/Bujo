from rest_framework import serializers
from .models import Diary


class DiaryEntrySerializer(serializers.ModelSerializer):
    user_id = serializers.UUIDField(source="user.public_id", read_only=True)

    class Meta:
        model = Diary
        fields = ["id", "title", "content", "date_created", "user_id", "date"]
        read_only_fields = ["user_id", "date_created"]  # REMOVE 'date' from here

    def validate_title(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Title is required.")
        return value

    def validate_content(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Content is required.")
        return value
