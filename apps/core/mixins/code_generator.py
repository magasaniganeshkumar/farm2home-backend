from django.db import models

from apps.core.utils.code_generator import generate_code


class CodeGeneratorMixin(models.Model):
    """
    Reusable business code mixin.

    Child models must define:

        code_prefix
        code_field
    """

    code_prefix = None
    code_field = None

    class Meta:
        abstract = True

    def generate_business_code(self):
        if not self.code_prefix:
            raise ValueError(
                "code_prefix must be defined."
            )

        if not self.code_field:
            raise ValueError(
                "code_field must be defined."
            )

        model = self.__class__

        last = (
            model.objects.order_by("-created_at")
            .only(self.code_field)
            .first()
        )

        if last:
            last_code = getattr(last, self.code_field)
            number = int(last_code.split("-")[-1]) + 1
        else:
            number = 1

        setattr(
            self,
            self.code_field,
            generate_code(
                self.code_prefix,
                number,
            ),
        )