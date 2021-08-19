from rest_framework import status
from rest_framework.test import APITestCase

from shortlinks.services import ShortLinkCreateService


class TestStatistics(APITestCase):
    URLS_IP_1_COUNT = 12
    URLS_IP_2_COUNT = 12

    def setUp(self) -> None:
        data = {
            "ip": "127.0.0.1",
            "url": "/test-redirect",
        }

        for i in range(self.URLS_IP_1_COUNT):
            ShortLinkCreateService(**data).execute()

        data["ip"] = "127.0.0.2"

        for i in range(self.URLS_IP_2_COUNT):
            ShortLinkCreateService(**data).execute()

    def test_count(self):
        response = self.client.get("/shortened_urls_count")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.content.decode(), "Number of shortened urls: 24"
        )

    def test_count_unique_visitors(self):
        response = self.client.get("/shortened_urls_count/unique")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.content.decode(), "Number of shortened urls: 2"
        )


class TestMostPopular(APITestCase):
    def setUp(self) -> None:
        self.sites = ["/site_" + str(i) for i in range(26)]
        self.sites_to_short = {k: v for v, k in enumerate(self.sites)}
        for site, _count in self.sites_to_short.items():
            for _ in range(_count):
                ShortLinkCreateService(ip="127.0.0.1", url=site).execute()

    def test_most_popular(self):
        response = self.client.get("/most_popular")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.content.decode(),
            "Most popular urls: " + ", ".join(list(reversed(self.sites))[:10]),
        )
