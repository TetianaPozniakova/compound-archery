# -*- coding: utf-8 -*-
from django.views.generic.dates import *
from kat_news.models import News
from taggit.models import Tag
from django.shortcuts import get_object_or_404


class NewsYearArchiveView(YearArchiveView):
    queryset = News.objects.all()
    date_field = "date"
    make_object_list = True
    allow_future = True


class NewsMonthArchiveView(MonthArchiveView):
    queryset = News.objects.all()
    date_field = "date"
    make_object_list = True
    allow_future = True


class NewsDayArchiveView(DayArchiveView):
    queryset = News.objects.all()
    date_field = "date"
    make_object_list = True
    allow_future = True


class TagListView(ArchiveIndexView):
    """
    Archive view for a given tag
    """

    # It probably makes more sense to set date_field here than in the url config
    # Ideally, set it in the parent HomePageView class instead of here.
    date_field = "date"

    def get_queryset(self):
        """
        Only include entries tagged with the selected tag
        """
        return News.objects.filter(tags__slug=self.kwargs['tag_slug'])

    def get_context_data(self, **kwargs):
        """
        Include the tag in the context
        """
        context_data = super(TagListView, self).get_context_data(**kwargs)
        context_data['tag'] = get_object_or_404(Tag, slug=self.kwargs['tag_slug'])
        return context_data