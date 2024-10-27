from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=40,
                                  blank=False,
                                  null=False
                                  )
    last_name = models.CharField(max_length=50,
                                 blank=False,
                                 null=False
                                 )
    passcode = models.CharField(max_length=6,
                                blank=False,
                                null=False
                                )
    pets_number = models.PositiveSmallIntegerField(blank=False,
                                                   null=False
                                                   )
    info = models.TextField(blank=True,
                            null=True
                            )
    image_url = models.URLField(blank=True,
                                null=True
                                )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
