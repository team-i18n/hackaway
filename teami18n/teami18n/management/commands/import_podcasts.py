from django.core.management.base import BaseCommand, CommandError

import requests
from django_countries.data import COUNTRIES
from email.utils import parsedate_tz
from datetime import datetime

from teami18n.models import Country, Podcast


class Command(BaseCommand):
    #args = '<poll_id poll_id ...>'
    help = 'Import Podcasts'

    def handle(self, *args, **options):
        for country in Country.objects.all():
            self.populate_podcasts(country)

    def populate_podcasts(self, country):
        country_name = unicode(COUNTRIES[country.code])
        print country_name
        url = ('http://api.npr.org/query?id=1001,1004'
               '&fields=title,teaser,show,image'
               '&requiredAssets=text,image,audio'
               '&dateType=story'
               '&startDate=2014-09-01'
               '&endDate=2014-10-04'
               '&searchTerm=' + country_name +
               '&sort=dateDesc'
               '&output=JSON'
               '&numResults=50'
               '&apiKey=MDE2ODkwMTczMDE0MTIwNjAxNDIxMGUxMA001')
        print url
        json = requests.get(url).json()
        for story in json["list"].get("story", []):
            show = story.get("show")
            podcast, _ = Podcast.objects.get_or_create(
                story_id=story['id'],
                link=story['link'][0]['$text'],
                title=story['title']['$text'],
                teaser=story['teaser']['$text'],
                program_name=self.program_name(show),
                show_date=self.show_date(show),
                image_link=story['image'][0]['src'])
            print podcast
            print
            podcast.countries.add(country)

    def program_name(self, show):
        if show:
            return show[0]['program']['$text']

    def show_date(self, show):
        if show:
            show_date = show[0]['showDate']['$text']
            return datetime(*parsedate_tz(show_date)[:6])
