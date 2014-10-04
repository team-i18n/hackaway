from datetime import date

from django.core.management import BaseCommand

import wbpy

from teami18n.models import Country


class Command(BaseCommand):
    help = 'Import Country Data'

    def handle(self, *args, **options):

        def get_population(country_code):
            current_date = date.today()
            last_year = str(current_date.year - 1)

            try:
                population_dataset = api.get_dataset(
                    "SP.POP.TOTL", [country_code], date=last_year)
                population = population_dataset.as_dict()[country_code][last_year]
                return population
            except ValueError:
                pass

        api = wbpy.IndicatorAPI()
        for country in Country.objects.all():
            population = get_population(country.code)
            if population:
                country.population = int(population)
                country.save()
