from django.db import models


class ActiveManager(models.Manager):
    """
    Returns only active (non-deleted) records.
    """

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class AllObjectsManager(models.Manager):
    """
    Returns all records, including soft-deleted ones.
    """

    def get_queryset(self):
        return super().get_queryset()
    
