from rest_framework import serializers

from apps.products.models import Category


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "code",
            "name",
            "slug",
            "image",
            "icon",
        )


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "code",
            "name",
            "slug",
            "description",
            "image",
            "icon",
            "seo_title",
            "seo_description",
        )