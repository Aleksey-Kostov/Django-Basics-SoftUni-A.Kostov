from django.db import models

from regular_exam_project.author.models import Author


class Post(models.Model):
    title = models.CharField(max_length=50,
                             unique=True,
                             null=False,
                             blank=False,
                             )
    image_url = models.URLField(null=False,
                                blank=False,
                                )
    content = models.TextField(null=False,
                               blank=False,
                               )
    updated_at = models.DateTimeField(auto_now=True,
                                      null=False,
                                      blank=False,
                                      )
    author = models.ForeignKey(to=Author,
                               on_delete=models.CASCADE
                               )

    def __str__(self):
        return self.title
