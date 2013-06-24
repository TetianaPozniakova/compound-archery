# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic import TemplateView, ListView, DateDetailView
from kat_main_site.models import Article


def main_page(request):
    return render_to_response('kat_main_page.html', RequestContext(request))


class ArticleDetailedView(DateDetailView):
    queryset = Article.objects.all()
    date_field = "article_publish_date"
    slug_field = "article_slug"
    make_object_list = True
    allow_future = True
