from django.db import models

from django_countries import countries
import humanize


class Country(models.Model):
    code = models.CharField(max_length=2, choices=tuple(countries),
                            unique=True)
    population = models.IntegerField(null=True, blank=True)
    podcasts_count = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.code

    @property
    def intword_population(self):
        return humanize.intword(self.population)

    def podcasts_per_captia(self):
        return float(self.podcasts_count) / float(self.population)

    def lastest_podcasts(self):
        return self.podcasts.order_by("-show_date")[:3]


class Podcast(models.Model):
    story_id = models.CharField(max_length=16, unique=True)
    link = models.URLField()
    title = models.TextField()
    teaser = models.TextField()
    program_name = models.TextField(null=True, blank=True)
    show_date = models.DateTimeField(null=True, blank=True)
    image_link = models.URLField(null=True, blank=True)

    countries = models.ManyToManyField(Country, related_name="podcasts")

    def __unicode__(self):
        return self.title
