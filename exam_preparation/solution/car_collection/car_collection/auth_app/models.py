from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from car_collection.core.validators import validate_chars_username


class Profile(models.Model):
    MAX_LEN_USERNAME = 15
    MIN_LEN_USERNAME = 3
    MAX_LEN_PASSWORD = 20
    MAX_LEN_F_NAME, MAX_LEN_L_NAME = 25, 25

    MIN_AGE = 21

    username = models.CharField(
        max_length=MAX_LEN_USERNAME,
        validators=(
            MinLengthValidator(MIN_LEN_USERNAME, message=f"Username must be at least {MIN_LEN_USERNAME} chars long!"),
            validate_chars_username,
        ),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=(MinValueValidator(MIN_AGE), )
    )

    password = models.CharField(
        max_length=MAX_LEN_PASSWORD,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_LEN_F_NAME,

        null=True,
        blank=True,
        verbose_name='First Name'
    )

    last_name = models.CharField(
        max_length=MAX_LEN_L_NAME,

        null=True,
        blank=True,
        verbose_name='Last Name'
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
        verbose_name='Profile Picture',
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        if self.first_name:
            return f'{self.first_name}'
        if self.last_name:
            return f'{self.last_name}'
        return None

