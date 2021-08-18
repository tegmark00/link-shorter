from rest_framework import serializers

from .models import ShortUrl
from .services import ShortLinkCreateService


class CreateShortUrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShortUrl
        fields = ('url',)

    def create(self, validated_data):
        return ShortLinkCreateService(
            ip=self.context['request'].META['REMOTE_ADDR'],
            url=validated_data['url']
        ).execute()
