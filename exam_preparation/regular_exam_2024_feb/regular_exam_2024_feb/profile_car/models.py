from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from regular_exam_2024_feb.profile_car.validators import AlphaNumericValidator


class Profile(models.Model):
    username = models.CharField(max_length=15,
                                validators=[MinLengthValidator(3, 'Username must be at least 3 chars long!'),
                                            AlphaNumericValidator()],
                                null=False,
                                blank=False,
                                )

    email = models.EmailField(null=False, blank=False,)

    age = models.IntegerField(validators=[MinValueValidator(21, 'Age requirement: 21 years and above.')],
                              null=False, blank=False
                              )

    password = models.CharField(null=False, blank=False, max_length=20,)

    first_name = models.CharField(max_length=25, null=True, blank=True,)

    last_name = models.CharField(max_length=25, null=True, blank=True)

    profile_picture = models.URLField(null=True, blank=True)



