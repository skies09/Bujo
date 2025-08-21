from django.urls import path
from accounts.user_profile import views

urlpatterns = [
    path("summary/", views.profile_summary, name="profile-summary"),
    path("public/<str:username>/", views.public_profile, name="public-profile"),
]
