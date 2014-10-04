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
               '&output=NPRML'
               '&numResults=10'
               '&apiKey=MDE2ODkwMTczMDE0MTIwNjAxNDIxMGUxMA001')
        print url
        print
        soup = BeautifulSoup(requests.get(url).text)
        for story in soup.find('story'):
            podcast, _ = Podcast.objects.get_or_create(
                story_id=story['id'],
                link=story.find('link', type="html").string,
                title=story.title.string,
                teaser=story.teaser.string,
                program_name=story.show.program.string,
                show_date=self.show_date(story),
                image_link=story.find('image', type="primary")["src"])
            print podcast
            podcast.countries.add(country)


    def show_date(self, story):
        if story.show.showdate:
            return datetime(*parsedate_tz(story.show.showdate.string)[:6])
