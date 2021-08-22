from django.http import HttpResponse
from rest_framework import status


class HttpTextResponse(HttpResponse):
    def __init__(self, content=b""):
        super().__init__(
            status=status.HTTP_200_OK,
            content_type="text",
        )
        self.content = content
