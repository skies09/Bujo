from rest_framework_nested import routers

from accounts.auth.viewsets import (
    RegisterViewSet,
    LoginViewSet,
    RefreshViewSet,
    LogoutViewSet,
)
from accounts.user.viewsets import UserViewSet
from accounts.diary.viewsets import DiaryEntryViewSet

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

urlpatterns = [*router.urls]
