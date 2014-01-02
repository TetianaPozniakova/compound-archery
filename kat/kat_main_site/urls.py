__author__ = 'noctule'
from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView, ListView, DateDetailView
from views import main_page, ArticleDetailedView, month, tournament_registration, participants_lists
from models import Article

urlpatterns = patterns('',
    (r'^$', 'kat_main_site.views.main_page'),
    (r'^news/', include('kat_news.urls')),

    # Static pages
    (r'^contacts/', TemplateView.as_view(template_name="kat_contacts_page.html")),

    (r'^history/', TemplateView.as_view(template_name="sport/kat_history_page.html")),
    (r'^development/', TemplateView.as_view(template_name="404.html")),
    (r'^rules/', TemplateView.as_view(template_name="sport/kat_rules_page.html")),
    (r'^literature/', TemplateView.as_view(template_name="sport/kat_literature_page.html")),
    (r'^faq/', TemplateView.as_view(template_name="sport/kat_faq_page.html")),
    url(r'^tournament-registration/', tournament_registration,
        name="tournament_registration"),
    (r'^participants-lists/', participants_lists),
    (r'^ranking/', TemplateView.as_view(template_name="competitions/kat_rating_page.html")),
    (r'^results/', TemplateView.as_view(template_name="competitions/kat_results_page.html")),
    (r'^records/', TemplateView.as_view(template_name="competitions/kat_records_page.html")),
    (r'^qualifying/', TemplateView.as_view(template_name="competitions/kat_qualifying_page.html")),

    (r'^organization/', TemplateView.as_view(template_name="404.html")),
    (r'^structure/', TemplateView.as_view(template_name="404.html")),
    (r'^activities/', TemplateView.as_view(template_name="404.html")),
    (r'^events/', TemplateView.as_view(template_name="404.html")),

    (r'^links/', TemplateView.as_view(template_name="kat_links_page.html")),

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