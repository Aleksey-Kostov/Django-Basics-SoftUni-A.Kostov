from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_name_starts_with_capital(value):
    if not value[0].isupper():
        raise ValidationError(_("Name must start with a capital letter!"))
