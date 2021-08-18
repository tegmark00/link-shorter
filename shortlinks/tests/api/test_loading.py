from timeit import timeit

from rest_framework.test import APITestCase


class TestLoadingCreate(APITestCase):

    def test_loading(self):

        def execute():
            self.client.post('/shorten_url', data={'url': '/test-redirect'})

        _t = timeit(lambda: execute(), number=1000)

        print(f"\n1k requests executed in: {round(_t, 2)} seconds.")  # ~ 1-1.5 seconds
