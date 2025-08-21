from rest_framework_nested import routers

from accounts.auth.viewsets import (
    RegisterViewSet,
    LoginViewSet,
    RefreshViewSet,
    LogoutViewSet,
)
from accounts.user.viewsets import UserViewSet
from accounts.diary.viewsets import DiaryEntryViewSet
from accounts.user_profile.viewsets import (
    AffirmationViewSet,
    GratitudeViewSet,
    PassionViewSet,
    FavoriteThingViewSet,
    AboutViewSet,
)

# Use DefaultRouter for browsable API support
router = routers.DefaultRouter()

# ---------------- AUTH ----------------
router.register(r"auth/register", RegisterViewSet, basename="auth-register")
router.register(r"auth/login", LoginViewSet, basename="auth-login")
router.register(r"auth/refresh", RefreshViewSet, basename="auth-refresh")
router.register(r"auth/logout", LogoutViewSet, basename="auth-logout")

# ---------------- USER ----------------
router.register(r"user", UserViewSet, basename="user")

# ---------------- DIARY ----------------
router.register(r"diary", DiaryEntryViewSet, basename="diary")

# ---------------- USER PROFILE ----------------
router.register(r"profile/affirmations", AffirmationViewSet, basename="affirmations")
router.register(r"profile/gratitudes", GratitudeViewSet, basename="gratitudes")
router.register(r"profile/passions", PassionViewSet, basename="passions")
router.register(r"profile/favorites", FavoriteThingViewSet, basename="favorites")
router.register(r"profile/about", AboutViewSet, basename="about")

urlpatterns = [*router.urls]
