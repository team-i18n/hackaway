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
        country_list = [(c.code, c.population) for c in countries]
        context["population_data"] = json.dumps(dict(country_list))
        return context
