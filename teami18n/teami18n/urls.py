from django.conf.urls import patterns, url
from django.views.static import serve
from django.conf import settings

from .views import HomeView

urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view(), name="home"),

    # Static files
    url(r'^static/(?P<path>.*)$', serve,
        kwargs={'document_root': settings.STATIC_ROOT})
)
