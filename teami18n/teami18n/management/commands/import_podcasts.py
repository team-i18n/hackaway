from django.core.management.base import BaseCommand

import requests
from django_countries.data import COUNTRIES
from email.utils import parsedate_tz
from datetime import datetime, date, timedelta
from urllib import quote

from teami18n.models import Country, Podcast


class Command(BaseCommand):
    help = 'Import yesterdays podcasts to keep map up to date.'

    def handle(self, *args, **options):
        for country in Country.objects.all():
            self.populate_podcasts(country)

    def populate_podcasts(self, country):
        print country.code
        yesterday = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
        country_name = self.country_name(country)
        url = ('http://api.npr.org/query?id=1001,1004'
               '&fields=title,teaser,show,image'
               '&requiredAssets=text,image,audio'
               '&dateType=story'
               '&date=' + yesterday +
               '&searchTerm=' + country_name +
               '&sort=dateDesc'
               '&output=JSON'
               '&numResults=50'
               '&apiKey=MDE2ODkwMTczMDE0MTIwNjAxNDIxMGUxMA001')
        # Change query to a date range to populate old data.
        #'&startDate=2012-01-01'
        #'&endDate=2013-12-31'
        json = requests.get(url).json()
        self.stories_to_podcasts(json, country)

    def stories_to_podcasts(self, json, country):
        for story in json["list"].get("story", []):
            show = story.get("show")
            podcast, was_created = Podcast.objects.get_or_create(
                story_id=story['id'],
                link=story['link'][0]['$text'],
                title=story['title']['$text'],
                teaser=story['teaser']['$text'],
                program_name=self.program_name(show),
                show_date=self.show_date(show),
                image_link=self.image(story))
            print podcast
            if was_created:
                podcast.countries.add(country)
                country.podcasts_count = country.podcasts_count + 1
                country.save()

    def image(self, story):
        image = story.get('image')
        if image:
            return image[0]['src']

    def country_name(self, country):
        if country.code == "CW":
            return "Cura%E7ao"
        elif country.code == "CI":
            return "C%F4te%20d%27Ivoire"
        elif country.code == "RE":
            return "R%E9union"
        elif country.code == "BL":
            return "Saint%20Barth%E9lemy"
        elif country.code == "AX":
            return "C5land%20Islands"
        else:
            return quote(unicode(COUNTRIES[country.code]))

    def program_name(self, show):
        if show:
            return show[0]['program']['$text']

    def show_date(self, show):
        if show:
            show_date = show[0]['showDate']['$text']
            return datetime(*parsedate_tz(show_date)[:6])
