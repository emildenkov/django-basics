from django.db import models


class LanguageChoices(models.TextChoices):
    ENGLISH = 'en', 'English'
    SPANISH = 'es', 'Spanish'
    ITALIAN = 'it', 'Italian'
    GERMAN = 'de', 'German'
    BULGARIAN = 'bu', 'Bulgarian'
