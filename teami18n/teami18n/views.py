import json
from django.views.generic import TemplateView

from .models import Country

# Countries Data:
# https://github.com/SmileyChris/django-countries/blob/master/django_countries/data.py#L45


class HomeView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        countries = Country.objects.filter(population__isnull=False)

        podcasts_per_captia_data = {
            c.code: c.podcasts_per_captia() for c in countries}
        podcasts_data = {c.code: c.podcasts_count() for c in countries}
        population_data = {c.code: c.population for c in countries}

        context["podcasts_per_captia_data"] = json.dumps(
            podcasts_per_captia_data)
        context["podcasts_data"] = json.dumps(podcasts_data)
        context["population_data"] = json.dumps(population_data)
        context["countries"] = countries
        return context
