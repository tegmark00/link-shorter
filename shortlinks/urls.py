from django.urls import path
from .views import CreateShortUrlView, RedirectUrlView, TestView, \
    StatisticsCountUrlsView, StatisticsCountUniqueVisitorsUrlsView, \
    MostPopularView

urlpatterns = [
    path('shorten_url', CreateShortUrlView.as_view()),
    path('test-redirect', TestView.as_view()),
    path('shortened_urls_count', StatisticsCountUrlsView.as_view()),
    path('shortened_urls_count/unique', StatisticsCountUniqueVisitorsUrlsView.as_view()),
    path('most_popular', MostPopularView.as_view()),
    path('<str:path>', RedirectUrlView.as_view()),
]
