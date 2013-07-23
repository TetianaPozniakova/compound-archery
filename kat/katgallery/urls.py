# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from katgallery.views import *
from django.views.generic.dates import *


urlpatterns = patterns('',
    url(r'^$', 'katgallery.views.gallery'),
    url(r'^album/(?P<album_id>\d+)/$', 'katgallery.views.album_list'),
)

