from django.conf.urls import patterns, include
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kat.views.home', name='home'),
    # url(r'^kat/', include('kat.foo.urls')),
    (r'^', include('kat_main_site.urls')),
    (r'^news/', include('kat_news.urls')),
    (r'^forum/', include('pybb.urls', namespace='pybb')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)