from django.contrib import admin

from apps.products.models import (
    Category,
    Product,
    SupplierProduct,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "name",
        "parent",
        "display_order",
        "is_featured",
        "is_active",
    )

    list_filter = (
        "is_active",
        "is_featured",
    )

    search_fields = (
        "code",
        "name",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }

    ordering = (
        "display_order",
        "name",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "product_code",
        "name",
        "category",
        "product_type",
        "default_unit",
        "status",
        "is_featured",
    )

    list_filter = (
        "status",
        "product_type",
        "category",
        "is_featured",
    )

    search_fields = (
        "product_code",
        "name",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }

    autocomplete_fields = (
        "category",
    )

    ordering = (
        "name",
    )


@admin.register(SupplierProduct)
class SupplierProductAdmin(admin.ModelAdmin):
    list_display = (
        "listing_code",
        "farmer",
        "product",
        "selling_price",
        "available_quantity",
        "status",
        "is_visible",
    )

    list_filter = (
        "status",
        "is_visible",
        "is_organic",
        "is_certified",
    )

    search_fields = (
        "listing_code",
        "product__name",
        "farmer__user__full_name",
    )

    autocomplete_fields = (
        "farmer",
        "product",
    )

    ordering = (
        "-created_at",
    )