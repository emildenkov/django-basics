from django.db import models


class Task(models.Model):
    name = models.CharField(
        max_length=50
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
