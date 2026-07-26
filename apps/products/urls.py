from django.urls import path

from apps.products.views import (
    CategoryDetailView,
    CategoryListView,
    MarketplaceProductDetailView,
    MarketplaceProductListView,
    ProductDetailView,
    ProductListView,
    SupplierProductDetailView,
    SupplierProductListCreateView,
)

urlpatterns = [
    # Categories
    path(
        "categories/",
        CategoryListView.as_view(),
        name="category-list",
    ),
    path(
        "categories/<uuid:pk>/",
        CategoryDetailView.as_view(),
        name="category-detail",
    ),

    # Product Catalog
    path(
        "products/",
        ProductListView.as_view(),
        name="product-list",
    ),
    path(
        "products/<uuid:pk>/",
        ProductDetailView.as_view(),
        name="product-detail",
    ),

    # Supplier Products
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

    # Marketplace
    path(
        "marketplace/products/",
        MarketplaceProductListView.as_view(),
        name="marketplace-product-list",
    ),
    path(
        "marketplace/products/<uuid:pk>/",
        MarketplaceProductDetailView.as_view(),
        name="marketplace-product-detail",
    ),
]