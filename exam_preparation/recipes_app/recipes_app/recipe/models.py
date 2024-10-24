from django.db import models

from recipes_app.profile_recipes.models import Profile
from recipes_app.recipe.choices import CuisineChoices


class Recipe(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True,
    )

    cuisine_type = models.CharField(
        choices=CuisineChoices,
        max_length=7,
    )

    ingredients = models.TextField(
        help_text="Ingredients must be separated by a comma and space.",
    )

    instructions = models.TextField()

    cooking_time = models.PositiveIntegerField(
        help_text="Provide the cooking time in minutes.",
    )

    image_url = models.URLField(
        blank=True,
    )

    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
