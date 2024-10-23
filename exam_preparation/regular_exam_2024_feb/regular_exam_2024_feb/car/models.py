from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from regular_exam_2024_feb.car.choices import GenreChoices
from regular_exam_2024_feb.car.validators import YearValidator
from regular_exam_2024_feb.profile_car.models import Profile


class Car(models.Model):
    type = models.CharField(max_length=10,
                            null=False,
                            blank=False,
                            choices=GenreChoices,
                            )

    model = models.CharField(max_length=15,
                             validators=[MinLengthValidator(1)],
                             blank=False,
                             null=False
                             )

    year = models.IntegerField(validators=[YearValidator()],
                               blank=False,
                               null=False
                               )

    image_url = models.URLField(unique=True,
                                null=False,
                                blank=False,
                                # help_text="https://...",
                                error_messages={
                                    'unique': "This image URL is already in use! Provide a new one."}
                                )

    price = models.FloatField(validators=[MinValueValidator(1.0)],
                              null=False,
                              blank=False, )

    owner = models.ForeignKey(to=Profile,
                              on_delete=models.CASCADE,
                              related_name='cars')
