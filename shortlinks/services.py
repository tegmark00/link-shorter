from secrets import token_urlsafe

from django.db import IntegrityError
from django.db.models import Count
from django.db.transaction import atomic

from .models import ShortUrl


class ShortLinkCreateService:
    def __init__(self, ip: str, url: str):
        self.ip = ip
        self.url = url

    def execute(self) -> ShortUrl:
        instance = ShortUrl(
            ip=self.ip,
            url=self.url,
        )
        return self._save(instance)

    @staticmethod
    def generate_random_path() -> str:
        return token_urlsafe(32)[:8]

    def _save(self, instance: ShortUrl) -> ShortUrl:
        try:
            with atomic():
                instance.path = self.generate_random_path()
                instance.save()
        except IntegrityError:
            self._save(instance)
        return instance


def get_total_shortened_urls() -> int:
    return ShortUrl.objects.count()


def get_number_unique_creators_shortened_urls() -> int:
    return ShortUrl.objects.values("ip").distinct().count()


def get_top10_popular_urls() -> tuple:
    return (
        ShortUrl.objects.values_list("url", flat=True)
        .annotate(url_count=Count("url"))
        .order_by("-url_count")[:10]
    )
