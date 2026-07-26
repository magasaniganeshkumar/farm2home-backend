from django.db import transaction
from django.db.models import F

from apps.infrastructure.models import BusinessSequence


class CodeService:
    """
    Service for generating sequential business codes.
    """

    @staticmethod
    @transaction.atomic
    def next(entity: BusinessSequence.Entity) -> str:
        sequence = (
            BusinessSequence.objects
            .select_for_update()
            .get(entity=entity)
        )

        sequence.last_number = F("last_number") + 1
        sequence.save(update_fields=["last_number"])

        sequence.refresh_from_db()

        return f"{sequence.prefix}-{sequence.last_number:06d}"

    @staticmethod
    def next_product_code():
        return CodeService.next(
            BusinessSequence.Entity.PRODUCT
        )

    @staticmethod
    def next_supplier_code():
        return CodeService.next(
            BusinessSequence.Entity.SUPPLIER
        )

    @staticmethod
    def next_order_code():
        return CodeService.next(
            BusinessSequence.Entity.ORDER
        )

    @staticmethod
    def next_payment_code():
        return CodeService.next(
            BusinessSequence.Entity.PAYMENT
        )