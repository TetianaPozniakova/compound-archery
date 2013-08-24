from django.shortcuts import render
from django.http import Http404
from katgallery.utils import get_albums, get_photos


def gallery(request):
    albums = get_albums()
    return render(request, 'gallery.html', {'albums': albums})


def album_list(request, album_id):
    for album in get_albums():
        if album.gphoto_id.text == album_id:
            photos = get_photos(album)
            return render(request, 'album.html', {'photos': photos, 'album': album })
    raise Http404()