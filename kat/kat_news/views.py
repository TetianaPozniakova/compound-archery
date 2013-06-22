# -*- coding: utf-8 -*-
from django.views.generic.dates import *
from kat_news.models import News


class ArticleYearArchiveView(YearArchiveView):
    queryset = News.objects.all()
    date_field = "date"
    make_object_list = True
    allow_future = True


class ArticleMonthArchiveView(MonthArchiveView):
    queryset = News.objects.all()
    date_field = "date"
    make_object_list = True
    allow_future = True


class ArticleDayArchiveView(DayArchiveView):
    queryset = News.objects.all()
    date_field = "date"
    make_object_list = True
    allow_future = True