from django.core.exceptions import ValidationError


def validate_chars_username(username):
    for ch in username:
        if not ch.isalnum() and ch != '_':
            raise ValidationError("Username must contain only letters, digits, and underscores!")