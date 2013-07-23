from django.conf import settings
from gdata.photos.service import PhotosService


PHOTO_THUMBSIZE = get('PICASAGALLERY_PHOTO_THUMBSIZE',  '128')
ALBUM_THUMBSIZE = get('PICASAGALLERY_ALBUM_THUMBSIZE', '160c')
PHOTO_IMGMAXSIZE = get('PICASAGALLERY_PHOTO_IMGMAXSIZE', '1024')


def get(key, default):
    return getattr(settings, key, default)


def get_albums():
    pws = PhotosService()
    uf = pws.GetUserFeed(user = settings.PICASAGALLERY_USER)
    feed = '{uri}&thumbsize={thumbsize}'.format(
        uri = uf.GetAlbumsUri(), thumbsize = ALBUM_THUMBSIZE
    )
    print feed
    return  pws.GetFeed(feed).entry


def get_photos(album):
    feed = '{uri}&imgmax={imgmax}&thumbsize={thumbsize}'.format(
        uri = album.GetPhotosUri(), imgmax = PHOTO_IMGMAXSIZE, thumbsize = PHOTO_THUMBSIZE
    )
    return PhotosService().GetFeed(feed).entry
