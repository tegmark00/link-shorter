from rest_framework import serializers

from .models import ShortUrl
from .services import ShortLinkCreateService
from .utils import get_ip_from_request


class CreateShortUrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShortUrl
        fields = ('url',)

    def create(self, validated_data):
        return ShortLinkCreateService(
            ip=get_ip_from_request(self.context['request']),
            url=validated_data['url']
        ).execute()
