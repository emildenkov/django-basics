from django.db import models
from forumApp.posts.choices import LanguageChoices


class Post(models.Model):
    title = models.CharField(
        max_length=50,
    )
    content = models.TextField()
    author = models.CharField(
        max_length=50,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    languages = models.CharField(
        max_length=30,
        choices=LanguageChoices,
    )