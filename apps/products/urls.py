from django.urls import path

from apps.products.views import (
    SupplierProductDetailView,
    SupplierProductListCreateView,
)

urlpatterns = [
    path(
        "supplier/products/",
        SupplierProductListCreateView.as_view(),
        name="supplier-product-list-create",
    ),
    path(
        "supplier/products/<uuid:pk>/",
        SupplierProductDetailView.as_view(),
        name="supplier-product-detail",
    ),
]