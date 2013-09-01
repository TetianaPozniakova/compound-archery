__author__ = 'noctule'
from django.conf.urls import patterns, url
from django.views.generic import TemplateView, ListView, DateDetailView
from kat_main_site.views import main_page, ArticleDetailedView, month
from kat_main_site.models import Article

urlpatterns = patterns('',
    # (r'^$', 'kat_main_site.views.main_page'),
    (r'^$', include('kat_news.urls')),

    # Static pages
    (r'^contacts/', TemplateView.as_view(template_name="contacts_page.html")),

)

urlpatterns += patterns('',
    url(r'^articles/$',
        ListView.as_view(queryset=Article.objects.published()),
        name='articles-index'),

    # url(r'^articles/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<article_slug>[-\w]+)/$',
    #     DateDetailView.as_view(model=Article, date_field='article_publish_date', slug_field='article_slug',
    #                            month_format="%m"),
    #     name='article-detail'),

    url(r'^articles/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
        ArticleDetailedView.as_view(month_format="%m"), name='article-detail'),
)

#Calendar
urlpatterns += patterns('kat_main_site.views',
    (r'^calendar/month/(\d+)/(\d+)/(prev|next)/$', 'month'),
    (r'^calendar/month/(\d+)/(\d+)/$', 'month'),
    (r'^calendar/month/$', 'month'),
)