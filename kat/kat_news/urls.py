# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from kat_news.models import News
from django.views.generic.dates import *
from kat_news.views import *
from kat import settings as news_settings


urlpatterns = patterns('',
    url(r'^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})-(?P<slug>[-\w]+)/$', DateDetailView.as_view(model=News, date_field="date", month_format='%m'), name='news_detail'),
)


if news_settings.ENABLE_NEWS_ARCHIVE_INDEX:
    urlpatterns += patterns('',
        url(r'^$', ArchiveIndexView.as_view(model=News, date_field="date"), name='news_archive_index'),
    )

if news_settings.ENABLE_NEWS_DATE_ARCHIVE:
    urlpatterns += patterns('',
        url(r'^archive/(?P<year>\d{4})/$', ArticleYearArchiveView.as_view(), name='news_archive_year'),
        url(r'^archive/(?P<year>\d{4})-(?P<month>\d{2})/$', ArticleMonthArchiveView.as_view(month_format='%m'), name='news_archive_month'),
        url(r'^archive/(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})/$', ArticleDayArchiveView.as_view(), name='news_archive_day'),
    )


urlpatterns += patterns('',
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', TagListView.as_view(paginate_by=5, template_name='news_archive_index.html')),
    )
