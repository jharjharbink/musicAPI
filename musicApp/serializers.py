from rest_framework.serializers import ModelSerializer
from musicApp.models import Albums


class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Albums
        fields = ('id',
                  'artist',
                  'album',
                  'album_creation_year',
                  'label',
                  'tags',
                  'published_date',
                  'comment_number',
                  'album_url',
                  'image_urls')
