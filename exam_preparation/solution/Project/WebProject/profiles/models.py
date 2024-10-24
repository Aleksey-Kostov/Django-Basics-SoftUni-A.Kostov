from django.core.validators import MinLengthValidator
from django.db import models
from WebProject.utils.validators import validate_name_starts_with_capital


# class Profile(models.Model):
#     username = models.CharField(
#         max_length=10,
#         validators=[
#             MinLengthValidator(2),
#         ]
#     )
#
#     first_name = models.CharField(
#         verbose_name="First Name",
#         max_length=20,
#         validators=[
#             profile_name_validator
#         ]
#     )
#
#     last_name = models.CharField(
#         verbose_name="Last Name",
#         max_length=20,
#         validators=[
#             profile_name_validator
#         ]
#     )
#
#     profile_picture = models.URLField(
#         verbose_name="Profile Picture",
#         null=True,
#         blank=True
#     )

class Profile(models.Model):
    MAX_LENGTH_NICK = 20
    MIN_LENGTH_NICK = 2
    MIN_LENGTH_NICK_MSG = "Nickname must be at least 2 chars long!"

    MAX_LENGTH_FLNames = 30

    nickname = models.CharField(
        max_length=MAX_LENGTH_NICK,
        unique=True,
        validators=[MinLengthValidator(MIN_LENGTH_NICK, message=MIN_LENGTH_NICK_MSG)]
    )
    first_name = models.CharField(
        max_length=MAX_LENGTH_FLNames,
        validators=[validate_name_starts_with_capital],
        verbose_name="First Name",
    )
    last_name = models.CharField(
        max_length=MAX_LENGTH_FLNames,
        validators=[validate_name_starts_with_capital],
        verbose_name="Last Name"

    )
    chef = models.BooleanField(
        default=False,
    )
    bio = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nickname