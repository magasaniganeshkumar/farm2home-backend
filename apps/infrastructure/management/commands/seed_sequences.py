from django.core.management.base import BaseCommand

from apps.infrastructure.models import BusinessSequence


class Command(BaseCommand):
    help = "Seed business sequences"

    SEQUENCES = [
        ("CATEGORY", "CAT"),
        ("PRODUCT", "PRD"),
        ("SUPPLIER", "SUP"),
        ("LISTING", "LST"),
        ("LOCATION", "LOC"),
        ("ORDER", "ORD"),
        ("PAYMENT", "PAY"),
    ]

    def handle(self, *args, **options):
        for entity, prefix in self.SEQUENCES:
            BusinessSequence.objects.get_or_create(
                entity=entity,
                defaults={
                    "prefix": prefix,
                    "last_number": 0,
                },
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Business sequences seeded successfully."
            )
        )