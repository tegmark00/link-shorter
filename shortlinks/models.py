from django.db import models


class ShortUrl(models.Model):
    ip = models.GenericIPAddressField()
    url = models.URLField()
    path = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return f"IP: {self.ip} Link: {self.url} Path: {self.path}"
