from django.db import models

from django_countries import countries


class Country(models.Model):
    code = models.CharField(max_length=2, choices=tuple(countries),
                            unique=True)

    def __unicode__(self):
        return self.code


class Podcast(models.Model):
    story_id = models.CharField(max_length=16, unique=True)
    link = models.URLField()
    title = models.TextField()
    teaser = models.TextField()
    program_name = models.TextField(blank=True)
    show_date = models.DateTimeField(null=True, blank=True)
    image_link = models.URLField(null=True, blank=True)

    countries = models.ManyToManyField(Country, related_name="podcasts")

    def __unicode__(self):
        return self.title
