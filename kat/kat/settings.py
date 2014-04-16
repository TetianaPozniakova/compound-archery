from django.conf import settings


DEBUG = True
#DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

try:
   from dev_settings import *
except ImportError:
   pass

ALLOWED_HOSTS = ['*.alwaysdata.net', 'compound-archery.com.ua']

TIME_ZONE = 'Europe/Kiev'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = False

USE_L10N = False

USE_TZ = True

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    #os.path.join(PROJECT_ROOT, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'pybb.middleware.PybbMiddleware',
    'account.middleware.LocaleMiddleware',
    'account.middleware.TimezoneMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'pybb.context_processors.processor',
    'account.context_processors.account',)

ROOT_URLCONF = 'kat.urls'

WSGI_APPLICATION = 'kat.wsgi.application'

import os
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),)

THUMBNAIL_FORMAT = "JPEG"

TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'theme_advanced_toolbar_location': "top",
    'remove_linebreaks': False,
    'convert_urls': False,
    'plugins': "preview",
    'width': '100%',
    'height': '300px',
    'paste_auto_cleanup_on_paste': True,
    'theme_advanced_buttons1': "formatselect, separator, bold, italic, underline, hr, separator, link, unlink,\
                                     separator, image, separator, bullist, numlist, separator, undo, redo,",
    'theme_advanced_buttons2': " fontselect, fontsizeselect, forecolor, backcolor, blockquote ",
    'theme_advanced_buttons3': "preview",
    'theme_advanced_blockformats': "p,h1,h2,h3,blockquote"
}

PYBB_TEMPLATE = 'kat_forum_base.html'
ACCOUNT_EMAIL_UNIQUE = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #Somehow example.com was deleted from somewhere
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.comments',
    'django.contrib.admin',
    'south',
    'sorl.thumbnail',
    'tinymce',
    'pybb',
    'pytils',
    'account',
    'pure_pagination',
    'pinax_theme_bootstrap_account',
    'pinax_theme_bootstrap',
    'django_forms_bootstrap',
    #'tagging',
    'taggit',
    'pagination',
    'kat_news',
    'gdata',
    'katgallery',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'kat_main_site',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

NEWS_TAGGING = getattr(settings, 'NEWS_TAGGING', True)
ENABLE_NEWS_LIST = getattr(settings, 'ENABLE_NEWS_LIST', False)
ENABLE_NEWS_ARCHIVE_INDEX = getattr(settings, 'ENABLE_NEWS_ARCHIVE_INDEX', True)
ENABLE_NEWS_DATE_ARCHIVE = getattr(settings, 'ENABLE_NEWS_DATE_ARCHIVE', True)

# Picasagallery settings
PICASAGALLERY_USER = 'compound.archeryua@gmail.com'
PICASAGALLERY_PHOTO_THUMBSIZE = '220'
PICASAGALLERY_PHOTO_IMGMAXSIZE = '1024'
PICASAGALLERY_ALBUM_THUMBSIZE = '220c'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/tmp/kat_cache',
        'TIMEOUT': 60 * 30,
    }
}