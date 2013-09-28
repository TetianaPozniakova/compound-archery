# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic import TemplateView, ListView, DateDetailView
from models import Article, CalendarEvent
from datetime import date, datetime, timedelta
import calendar
import time


def main_page(request):
    return render_to_response('kat_main_page.html', RequestContext(request))


class ArticleDetailedView(DateDetailView):
    queryset = Article.objects.all()
    date_field = "article_publish_date"
    slug_field = "article_slug"
    make_object_list = True
    allow_future = True


#Calendar Views
mnames = "January February March April May June July August September October November December"
mnames = mnames.split()


def month(request, year, month, change=None):
    """Listing of days in `month`."""
    year, month = int(year), int(month)

    # apply next / previous change
    if change in ("next", "prev"):
        now, mdelta = date(year, month, 15), timedelta(days=31)
        if change == "next":   mod = mdelta
        elif change == "prev": mod = -mdelta

        year, month = (now+mod).timetuple()[:2]

    # init variables
    cal = calendar.Calendar()
    month_days = cal.itermonthdays(year, month)
    nyear, nmonth, nday = time.localtime()[:3]
    lst = [[]]
    week = 0

    # make month lists containing list of days for each week
    # each day tuple will contain list of entries and 'current' indicator
    for day in month_days:
        entries = current = False   # are there entries for this day; current day?
        if day:
            entries = CalendarEvent.objects.filter(event_start_date__year=year, event_start_date__month=month, event_start_date__day=day)
            if day == nday and year == nyear and month == nmonth:
                current = True

        lst[week].append((day, entries, current))
        if len(lst[week]) == 7:
            lst.append([])
            week += 1

    return render_to_response("calendar/kat_calendar_month_view.html", dict(year=year, month=month,
                        month_days=lst, mname=mnames[month-1]))