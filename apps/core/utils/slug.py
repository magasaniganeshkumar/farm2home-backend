from django.utils.text import slugify


def generate_slug(value: str) -> str:
    """
    Generate a URL-friendly slug.
    """
    return slugify(value)