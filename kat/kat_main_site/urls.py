__author__ = 'noctule'
from django.conf.urls import patterns, url
from django.views.generic import TemplateView, ListView, DateDetailView
from kat_main_site.views import main_page
from kat_main_site.models import Article

urlpatterns = patterns('',
    (r'^$', 'kat_main_site.views.main_page'),

    # Static pages
    (r'^contacts/', TemplateView.as_view(template_name="contacts_page.html")),

)

urlpatterns += patterns('',
    url(r'^articles/',
        ListView.as_view(queryset=Article.objects.published()),
        name='articles-index'),

    url(r'^articles/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
        DateDetailView.as_view(model=Article, date_field='article_publish_date',
                               month_format="%m"),
        name='article-detail'),
    )