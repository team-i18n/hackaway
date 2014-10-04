from django.core.management.base import BaseCommand, CommandError

from bs4 import BeautifulSoup
import requests
from django_countries.data import COUNTRIES

from teami18n.models import Country, Podcast


class Command(BaseCommand):
    #args = '<poll_id poll_id ...>'
    help = 'Import Podcasts'

    def handle(self, *args, **options):
        for country in Country.objects.all():
            self.populate_podcasts(country)

    def populate_podcasts(country):
        country_name = unicode(COUNTRIES[country.code])
        url = ('http://api.npr.org/query?id=1001,1004'
               '&fields=title,teaser,show,image'
               '&requiredAssets=text,image,audio'
               '&dateType=story'
               '&startDate=2014-10-01'
               '&endDate=2014-10-31'
               '&searchTerm=' + country_name +
               '&sort=dateDesc'
               '&output=NPRML'
               '&numResults=50'
               '&apiKey=MDE2ODkwMTczMDE0MTIwNjAxNDIxMGUxMA001')
        soup = BeautifulSoup(requests.get(url).text)
        for story in soup.find_all('story'):
            podcast = Podcast.objects.get_or_create(
                story_id=story['id'],
                link=story.find('link', type="html").string,
                title=story.title.string,
                teaser=story.teaser.string,
                program_name=story.show.program.string,
                show_date=story.show.showdate.string,  #TODO: to datetime?
                image_link=story.find('image', type="primary")["src"])
            podcast.countries.add(country)
