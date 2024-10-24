from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator

from WebProject.profiles.models import Profile


class Recipe(models.Model):
    MAX_LENGTH_TITLE = 100
    MIN_LENGTH_TITLE = 10

    MAX_LENGTH_CUISINE_TYPE = 7

    MIN_VALUE_TIME = 1

    CUISINE_CHOICES = [
        ('French', 'French'),
        ('Chinese', 'Chinese'),
        ('Italian', 'Italian'),
        ('Balkan', 'Balkan'),
        ('Other', 'Other')
    ]

    title = models.CharField(
        max_length=MAX_LENGTH_TITLE,
        unique=True,
        validators=[MinLengthValidator(MIN_LENGTH_TITLE)],
    )
    cuisine_type = models.CharField(
        max_length=MAX_LENGTH_CUISINE_TYPE,
        choices=CUISINE_CHOICES,
        verbose_name="Cuisine Type"
    )
    ingredients = models.TextField(
    )

    instructions = models.TextField(
    )
    cooking_time = models.PositiveIntegerField(
        validators=[MinValueValidator(MIN_VALUE_TIME)],
        verbose_name="Cooking Time",
    )
    image_url = models.URLField(
        blank=True,
        null=True,
        verbose_name="Image URL"
    )
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title