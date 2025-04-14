from django.core.exceptions import ValidationError
import re

def validate_phone(value):
    """
    Validates phone number format.
    """
    if not re.match(r'^\+?\d{10,15}$', value):
        raise ValidationError("Invalid phone number format.")

def validate_positive(value):
    """
    Ensure a value is positive.
    """
    if value <= 0:
        raise ValidationError("Value must be positive.")
