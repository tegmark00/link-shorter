from unittest.mock import patch

from django.conf import settings
from rest_framework import status
from rest_framework.test import APITestCase

from shortlinks.models import ShortUrl


class TestCreateShortUrl(APITestCase):
    IP = "127.0.0.1"
    GENERATED_PATH = "foo"

    def setUp(self) -> None:
        self.endpoint = "/shorten_url"
        self.url = "https://127.0.0.1"

    def _request(self):
        data = {"url": self.url}
        return self.client.post(self.endpoint, data=data, format="json")

    @patch("shortlinks.serializers.ShortLinkCreateService.execute")
    def test_service_execution(self, service_execute_mock):
        _obj = ShortUrl(ip=self.IP, url=self.url, path=self.GENERATED_PATH)
        service_execute_mock.return_value = _obj
        response = self._request()
        service_execute_mock.assert_called()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    @patch(
        "shortlinks.serializers.ShortLinkCreateService.generate_random_path"
    )
    def test_response_body(self, generate_path_mock):
        generate_path_mock.return_value = self.GENERATED_PATH
        response = self._request()
        generate_path_mock.assert_called()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.json(),
            {
                "shortened_url": settings.WEBSITE_URL
                + "/"
                + self.GENERATED_PATH
            },
        )

    def test_invalid_url(self):
        self.url = "/some-url"
        response = self._request()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {"url": ["Enter a valid URL."]})
