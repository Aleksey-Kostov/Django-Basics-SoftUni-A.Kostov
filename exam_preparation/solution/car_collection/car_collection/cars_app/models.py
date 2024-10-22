from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from car_collection.auth_app.models import Profile


class Car(models.Model):
    MAX_LEN_TYPE = 10

    MAX_LEN_MODEL = 15
    MIN_LEN_MODEL = 1

    MIN_YEAR = 1999
    MAX_YEAR = 2030

    MIN_PRICE = 1.0

    ERROR_MESSAGE_YEAR = f"Year must be between {MIN_YEAR} and {MAX_YEAR}!"

    OPTIONS_LIST = ["Rally", "Open-wheel", "Kart", "Drag", "Other"]
    CHOICES = tuple([(c, c) for c in OPTIONS_LIST])

    type = models.CharField(
        max_length=MAX_LEN_TYPE,
        null=False,
        blank=False,

        choices=CHOICES,
    )

    model = models.CharField(
        max_length=MAX_LEN_MODEL,
        validators=(MinLengthValidator(MIN_LEN_MODEL),),
        null=False,
        blank=False,

    )

    year = models.IntegerField(
        validators=(MaxValueValidator(MAX_YEAR, message=ERROR_MESSAGE_YEAR),
                    MinValueValidator(MIN_YEAR, message=ERROR_MESSAGE_YEAR),),
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        unique=True,
        verbose_name='Image URL'
    )

    price = models.FloatField(
        validators=(
            MinValueValidator(MIN_PRICE),
        ),
        null=False,
        blank=False,

    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        blank=True,
        null=False,
    )
