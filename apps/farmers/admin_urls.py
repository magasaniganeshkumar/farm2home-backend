from django.urls import path

from .views import (
    AdminSupplierListView,
    AdminSupplierDetailView,
    AdminVerifySupplierView,
    AdminRejectSupplierView,
)

urlpatterns = [
    path(
        "farmers/",
        AdminSupplierListView.as_view(),
        name="admin-supplier-list",
    ),
    path(
        "farmers/<uuid:pk>/",
        AdminSupplierDetailView.as_view(),
        name="admin-supplier-detail",
    ),
    path(
        "farmers/<uuid:pk>/verify/",
        AdminVerifySupplierView.as_view(),
        name="admin-supplier-verify",
    ),
    path(
        "farmers/<uuid:pk>/reject/",
        AdminRejectSupplierView.as_view(),
        name="admin-supplier-reject",
    ),
]