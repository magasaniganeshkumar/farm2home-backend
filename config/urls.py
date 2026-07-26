from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

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

    path(
        "api/v1/admin/",
        include("apps.farmers.admin_urls"),
    ),
    path(
        "api/v1/",
        include("apps.products.urls"),
    ),
    

]

if settings.DEBUG:
        urlpatterns += static(
            settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT,
    )