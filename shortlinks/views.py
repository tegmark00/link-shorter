from django.conf import settings
from django.db.models import Count
from django.http import HttpResponse
from django.views.generic import RedirectView
from rest_framework import status
from rest_framework.generics import GenericAPIView, CreateAPIView, get_object_or_404
from rest_framework.response import Response

from .serializers import CreateShortUrlSerializer
from .models import ShortUrl
from .utils import get_host_from_request


class CreateShortUrlView(CreateAPIView):
    serializer_class = CreateShortUrlSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        url = get_host_from_request(request) + '/' + serializer.instance.path
        return Response({
            'shortened_url': url
        }, status=status.HTTP_201_CREATED, headers=headers)


class RedirectUrlView(RedirectView):

    def get_redirect_url(self, path):
        short_url = get_object_or_404(ShortUrl, path=path)
        return short_url.url


class TestView(GenericAPIView):

    def get(self, request, *args, **kwargs):
        return HttpResponse(
            'It works', status=status.HTTP_200_OK, content_type='text'
        )


class StatisticsCountUrlsView(GenericAPIView):

    def _get_count(self):
        return ShortUrl.objects.count()

    def get(self, request, *args, **kwargs):
        return HttpResponse(
            f'Number of shortened urls: {self._get_count()}',
            status=status.HTTP_200_OK,
            content_type='text'
        )


class StatisticsCountUniqueVisitorsUrlsView(StatisticsCountUrlsView):

    def _get_count(self):
        return ShortUrl.objects.values('ip').distinct().count()


class MostPopularView(GenericAPIView):

    def get(self, request, *args, **kwargs):
        top_urls = ShortUrl.objects.values_list('url', flat=True).annotate(
            url_count=Count('url')
        ).order_by('-url_count')[:10]

        top_urls = ', '.join(list(top_urls))

        return HttpResponse(
            f'Most popular urls: {top_urls}',
            status=status.HTTP_200_OK,
            content_type='text'
        )
