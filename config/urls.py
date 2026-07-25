from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    # Django Admin
    path("admin/", admin.site.urls),

    # API Documentation
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),

    # Accounts API
    path(
        "api/v1/accounts/",
        include("apps.accounts.urls"),
    ),  
    path(
        "api/v1/locations/",
        include("apps.locations.urls"),
    ),
    path(
        "api/v1/farmers/",
        include("apps.farmers.urls"),
    ),
]