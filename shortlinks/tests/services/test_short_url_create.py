from unittest.mock import patch
from django.test import TestCase

from shortlinks.services import ShortLinkCreateService
from shortlinks.models import ShortUrl


class TestShortLinkCreateService(TestCase):

    def setUp(self) -> None:
        self.ip = '127.0.0.1'
        self.url = 'https://google.com'
        self.service = ShortLinkCreateService(ip=self.ip, url=self.url)

    def test_random_generating(self):
        path = self.service.generate_random_path()
        new_path = self.service.generate_random_path()
        self.assertNotEqual(path, new_path)

    def test_path_length(self):
        path = self.service.generate_random_path()
        self.assertTrue(len(path) == 8)

    def test_created(self):
        self.assertTrue(ShortUrl.objects.count() == 0)
        instance = self.service.execute()
        self.assertTrue(ShortUrl.objects.count() == 1)
        self.assertTrue(instance.pk is not None)
        self.assertEqual(self.ip, instance.ip)
        self.assertEqual(self.url, instance.url)

    @patch('shortlinks.services.ShortLinkCreateService.generate_random_path')
    def test_integrity_error(self, generate_random_path_mock):
        generate_random_path_mock.side_effect = ['foo', 'foo', 'bar', 'baz']
        self.service.execute()
        self.service.execute()
        self.service.execute()
        self.assertEqual(generate_random_path_mock.call_count, 4)
        self.assertTrue(ShortUrl.objects.count() == 3)


