from secrets import token_urlsafe

from django.db import IntegrityError
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
