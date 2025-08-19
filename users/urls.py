from django.urls import path

from users.views import (
    LoginUserView,
    LogoutUserView,
    ProfessionCreateAPIView,
    ProfessionDestroyAPIView,
    ProfessionListAPIView,
    ProfessionRetrieveAPIView,
    ProfessionUpdateAPIView,
    ProfileUpdateView,
    RegisterUserView,
    UserDetailAPIView,
    UserListAPIView,
    UserProfileAPIView,
)

urlpatterns = [
    # APIs
    path("", UserListAPIView.as_view(), name="user-list"),
    path("<int:pk>/", UserDetailAPIView.as_view(), name="user-detail"),
    path("profile/", UserProfileAPIView.as_view(), name="profile"),
    path("professions/", ProfessionListAPIView.as_view(), name="professions"),
    path(
        "professions/<int:id>/",
        ProfessionRetrieveAPIView.as_view(),
        name="profession-detail",
    ),
    path(
        "professions/<int:id>/update/",
        ProfessionUpdateAPIView.as_view(),
        name="profession-update",
    ),
    path(
        "professions/<int:id>/delete/",
        ProfessionDestroyAPIView.as_view(),
        name="profession-delete",
    ),
    path(
        "professions/create/",
        ProfessionCreateAPIView.as_view(),
        name="profession-create",
    ),
    # Templates
    path("template/register/", RegisterUserView.as_view(), name="register-template"),
    path("template/login/", LoginUserView.as_view(), name="login-template"),
    path("template/logout/", LogoutUserView.as_view(), name="logout-template"),
    path("template/profile/", ProfileUpdateView.as_view(), name="profile-template"),
]
