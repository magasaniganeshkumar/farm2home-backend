from django.db import models

from apps.core.utils.slug import generate_slug


class SlugMixin(models.Model):
    """
    Reusable slug mixin.

    Child models must define:

        slug_source_field = "name"
    """

    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        db_index=True,
    )

    slug_source_field = "name"

    class Meta:
        abstract = True

    def generate_slug(self):
        value = getattr(self, self.slug_source_field)
        self.slug = generate_slug(value)