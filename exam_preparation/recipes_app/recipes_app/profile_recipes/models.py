from django.db import models


class Profile(models.Model):
    nickname = models.CharField(
        max_length=20,
        unique=True,
    )

    first_name = models.CharField(
        max_length=30,
    )

    last_name = models.CharField(
        max_length=30,
    )

    chef = models.BooleanField(
        default=False,
    )

    bio = models.TextField(
        blank=True,
    )
