from django.urls import path

from .views import (
    LocationListCreateView,
    LocationRetrieveUpdateDestroyView,
)

app_name = "locations"

urlpatterns = [
    path(
        "",
        LocationListCreateView.as_view(),
        name="location-list-create",
    ),
    path(
        "<uuid:pk>/",
        LocationRetrieveUpdateDestroyView.as_view(),
        name="location-detail",
    ),
]