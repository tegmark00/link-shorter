from rest_framework import status
from rest_framework.test import APITestCase

from shortlinks.models import ShortUrl


class TestCreateShortUrl(APITestCase):
    def setUp(self) -> None:
        self.short_url = ShortUrl.objects.create(
            ip="127.0.0.1",
            url="/test-redirect",
            path="aaaaaa",
        )
        self.url = "/aaaaaa"

    def test_redirect(self):
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.content.decode(), "It works")

    def test_not_found(self):
        response = self.client.get("/invalid", follow=True)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
