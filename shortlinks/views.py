from django.views.generic import RedirectView
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.generics import GenericAPIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import ShortUrl
from .responses import HttpTextResponse
from .serializers import CreateShortUrlSerializer
from .services import get_number_unique_creators_shortened_urls
from .services import get_top10_popular_urls
from .services import get_total_shortened_urls
from .utils import get_host_from_request


class CreateShortUrlView(CreateAPIView):
    serializer_class = CreateShortUrlSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        url = get_host_from_request(request) + "/" + serializer.instance.path
        return Response({"shortened_url": url}, status=status.HTTP_201_CREATED)


class RedirectUrlView(RedirectView):
    def get_redirect_url(self, path):
        short_url = get_object_or_404(ShortUrl, path=path)
        return short_url.url


class StatisticsCountUrlsView(GenericAPIView):
    def get(self, request, *args, **kwargs):
        _count = get_total_shortened_urls()
        return HttpTextResponse(
            f"Number of shortened urls: {_count}",
        )


class StatisticsCountUniqueCreatorsUrlsView(StatisticsCountUrlsView):
    def get(self, request, *args, **kwargs):
        _count = get_number_unique_creators_shortened_urls()
        return HttpTextResponse(
            f"Number of shortened urls: {_count}",
        )


class MostPopularView(GenericAPIView):
    def get(self, request, *args, **kwargs):
        top_urls = get_top10_popular_urls()
        top_urls = ", ".join(list(top_urls))
        return HttpTextResponse(
            f"Most popular urls: {top_urls}",
        )


class TestView(GenericAPIView):
    def get(self, request, *args, **kwargs):
        return HttpTextResponse("It works")
