from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from kat_main_site.forms import SignupFormWithCaptcha
from kat_main_site.views import video_list

from account.views import ChangePasswordView, SignupView, LoginView


# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kat.views.home', name='home'),
    # url(r'^kat/', include('kat.foo.urls')),
    (r'^', include('kat_main_site.urls')),
    (r'^news/', include('kat_news.urls')),
    (r'^gallery/', include('katgallery.urls')),
    (r'^video/$', video_list),


    url(r"^accounts/password/$", ChangePasswordView.as_view(), name="auth_password_change"),
    url(r"^accounts/signup/$", SignupView.as_view(form_class=SignupFormWithCaptcha), name="registration_register"),
    url(r"^accounts/login/$", LoginView.as_view(), name="auth_login"),

    (r'^accounts/', include('account.urls')),

    (r'^forum/', include('pybb.urls', namespace='pybb')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^arrows/', include(admin.site.urls)),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)