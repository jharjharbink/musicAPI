from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from musicApp.models import Albums
from musicApp.serializers import AlbumSerializer


@csrf_exempt
def AlbumAPI(request, id=0):
    if request.method == 'GET':
        album = Albums.objects.all()
        album_serializer = AlbumSerializer(album, many=True)
        return JsonResponse(album_serializer.data, safe=False)
