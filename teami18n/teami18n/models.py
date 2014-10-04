from django.db import models

from django_countries import countries


class Country(models.Model):
    code = models.CharField(max_length=2, choices=tuple(countries),
                            unique=True)
    population = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.code

    def podcasts_per_captia(self):
        if self.population:
            podcasts = self.podcasts.all().count()
            return podcasts / self.population


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
