from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from django.shortcuts import get_object_or_404

from accounts.user_profile.models import (
    Affirmation,
    Gratitude,
    Passion,
    FavoriteThing,
    About,
)
from accounts.user_profile.serializers import (
    AffirmationSerializer,
    GratitudeSerializer,
    PassionSerializer,
    FavoriteThingSerializer,
    AboutSummarySerializer,
)


# Create your views here.


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def profile_summary(request):
    """Get a summary of user's profile data"""
    user = request.user

    summary = {
        "affirmations": {
            "count": Affirmation.objects.filter(user=user, is_active=True).count(),
            "recent": AffirmationSerializer(
                Affirmation.objects.filter(user=user, is_active=True).order_by(
                    "-created"
                )[:5],
                many=True,
            ).data,
        },
        "gratitudes": {
            "count": Gratitude.objects.filter(user=user, is_active=True).count(),
            "recent": GratitudeSerializer(
                Gratitude.objects.filter(user=user, is_active=True).order_by(
                    "-created"
                )[:5],
                many=True,
            ).data,
        },
        "passions": {
            "count": Passion.objects.filter(user=user, is_active=True).count(),
            "recent": PassionSerializer(
                Passion.objects.filter(user=user, is_active=True).order_by("-created")[
                    :5
                ],
                many=True,
            ).data,
        },
        "favorites": {
            "count": FavoriteThing.objects.filter(user=user, is_active=True).count(),
            "by_category": FavoriteThing.objects.filter(user=user, is_active=True)
            .values("category")
            .annotate(count=Count("id")),
            "recent": FavoriteThingSerializer(
                FavoriteThing.objects.filter(user=user, is_active=True).order_by(
                    "-created"
                )[:5],
                many=True,
            ).data,
        },
    }

    return Response(summary)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def public_profile(request, username):
    """Get public profile information for a user"""
    from accounts.user.models import User

    user = get_object_or_404(User, username=username)

    # Get public about section
    try:
        about = About.objects.get(user=user, is_public=True)
        about_data = AboutSummarySerializer(about).data
    except About.DoesNotExist:
        about_data = None

    # Get public favorites (only active ones)
    public_favorites = FavoriteThing.objects.filter(user=user, is_active=True).order_by(
        "category", "order"
    )

    favorites_by_category = {}
    for favorite in public_favorites:
        category = favorite.get_category_display()
        if category not in favorites_by_category:
            favorites_by_category[category] = []
        favorites_by_category[category].append(FavoriteThingSerializer(favorite).data)

    profile_data = {
        "username": user.username,
        "name": user.name,
        "about": about_data,
        "favorites": favorites_by_category,
        "has_public_profile": about_data is not None or public_favorites.exists(),
    }

    return Response(profile_data)
