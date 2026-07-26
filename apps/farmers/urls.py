from django.urls import path

from .views import (
    SupplierApplicationView,
    FarmerListView,
    MySupplierProfileView,
    SupplierStatusView,
)

urlpatterns = [
    path(
        "apply/",
        SupplierApplicationView.as_view(),
        name="supplier-apply",
    ),
    path(
        "me/",
        MySupplierProfileView.as_view(),
        name="supplier-profile",
    ),
    path(
        "status/",
        SupplierStatusView.as_view(),
        name="supplier-status",
    ),
    path(
        "",
        FarmerListView.as_view(),
        name="farmer-list",
    ),
]