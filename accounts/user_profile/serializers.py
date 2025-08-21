from rest_framework import serializers
from accounts.abstract.serializers import AbstractSerializer
from accounts.user_profile.models import Affirmation, Gratitude, Passion, FavoriteThing, About


class AffirmationSerializer(AbstractSerializer):
    
    class Meta:
        model = Affirmation
        fields = [
            "id",
            "text",
            "is_active",
            "order",
            "created",
            "updated",
        ]
        read_only_fields = ["id", "created", "updated"]


class GratitudeSerializer(AbstractSerializer):
    
    class Meta:
        model = Gratitude
        fields = [
            "id",
            "text",
            "is_active",
            "order",
            "created",
            "updated",
        ]
        read_only_fields = ["id", "created", "updated"]


class PassionSerializer(AbstractSerializer):
    
    class Meta:
        model = Passion
        fields = [
            "id",
            "text",
            "is_active",
            "order",
            "created",
            "updated",
        ]
        read_only_fields = ["id", "created", "updated"]


class FavoriteThingSerializer(AbstractSerializer):
    category_display = serializers.CharField(source='get_category_display', read_only=True)
    
    class Meta:
        model = FavoriteThing
        fields = [
            "id",
            "category",
            "category_display",
            "title",
            "description",
            "is_active",
            "order",
            "created",
            "updated",
        ]
        read_only_fields = ["id", "created", "updated"]


class AboutSerializer(AbstractSerializer):
    display_name = serializers.CharField(source='get_display_name', read_only=True)
    summary = serializers.CharField(source='get_summary', read_only=True)
    
    class Meta:
        model = About
        fields = [
            "id",
            "nickname",
            "pronouns",
            "location",
            "occupation",
            "education",
            "personality_type",
            "zodiac_sign",
            "life_goals",
            "personal_mission",
            "hobbies",
            "interests",
            "lifestyle_preferences",
            "personal_story",
            "achievements",
            "challenges_overcome",
            "core_values",
            "beliefs",
            "philosophy",
            "relationship_status",
            "family_info",
            "social_preferences",
            "career_goals",
            "skills",
            "work_style",
            "health_goals",
            "fitness_preferences",
            "wellness_practices",
            "creative_interests",
            "artistic_preferences",
            "self_expression",
            "bucket_list",
            "dreams_aspirations",
            "future_plans",
            "notes",
            "is_public",
            "display_name",
            "summary",
            "created",
            "updated",
        ]
        read_only_fields = ["id", "created", "updated"]


class AboutSummarySerializer(AbstractSerializer):
    """Simplified serializer for public profile display"""
    display_name = serializers.CharField(source='get_display_name', read_only=True)
    summary = serializers.CharField(source='get_summary', read_only=True)
    
    class Meta:
        model = About
        fields = [
            "id",
            "nickname",
            "location",
            "occupation",
            "personality_type",
            "hobbies",
            "interests",
            "personal_mission",
            "core_values",
            "display_name",
            "summary",
        ]
        read_only_fields = ["id"]
