from django.urls import path

from .views import CreateShortUrlView
from .views import MostPopularView
from .views import RedirectUrlView
from .views import StatisticsCountUniqueCreatorsUrlsView
from .views import StatisticsCountUrlsView
from .views import TestView

urlpatterns = [
    path("shorten_url", CreateShortUrlView.as_view()),
    path("test-redirect", TestView.as_view()),
    path("shortened_urls_count", StatisticsCountUrlsView.as_view()),
    path(
        "shortened_urls_count/unique",
        StatisticsCountUniqueCreatorsUrlsView.as_view(),
    ),
    path("most_popular", MostPopularView.as_view()),
    path("<str:path>", RedirectUrlView.as_view()),
]
