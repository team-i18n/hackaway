from django.db import models

from django_countries import countries


class Country(models.Model):
    code = models.CharField(max_length=2, choices=tuple(countries))
