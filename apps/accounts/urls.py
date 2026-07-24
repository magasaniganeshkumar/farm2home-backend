from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    ChangePasswordView,
    ForgotPasswordView,
    ResetPasswordView,
    UserLoginView,
    UserLogoutView,
    UserProfileView,
    UserRegistrationView,
)

app_name = "accounts"

urlpatterns = [
    path(
        "register/",
        UserRegistrationView.as_view(),
        name="register",
    ),
    path(
        "login/",
        UserLoginView.as_view(),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path(
        "me/",
        UserProfileView.as_view(),
        name="profile",
    ),
    path(
        "logout/",
        UserLogoutView.as_view(),
        name="logout",
    ),
    path(
        "change-password/",
        ChangePasswordView.as_view(),
        name="change-password",
    ),
    path(
        "forgot-password/",
        ForgotPasswordView.as_view(),
        name="forgot-password",
    ),
    path(
        "reset-password/",
        ResetPasswordView.as_view(),
        name="reset-password",
    ),
]