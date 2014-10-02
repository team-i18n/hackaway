from django.views.generic import TemplateView

# Countries Data:
# https://github.com/SmileyChris/django-countries/blob/master/django_countries/data.py#L45


class HomeView(TemplateView):
    template_name = "base.html"
