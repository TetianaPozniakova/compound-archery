# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.template import RequestContext
from django.views.generic import TemplateView, ListView, DateDetailView
from models import Participant, CompetitionRegistration, Tournament
from models import Article, CalendarEvent, Video
from kat_news.models import News
from datetime import date, datetime, timedelta
import calendar
import time


def main_page(request):
    if News.objects.all().count():
        return redirect("/news/")
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
            entries = CalendarEvent.objects.filter(event_start_date__year=year, event_start_date__month=month,
                                                   event_start_date__day=day)
            if day == nday and year == nyear and month == nmonth:
                current = True

        lst[week].append((day, entries, current))
        if len(lst[week]) == 7:
            lst.append([])
            week += 1

    return render_to_response("calendar/kat_calendar_month_view.html", dict(year=year, month=month,
                                                                            month_days=lst, mname=mnames[month-1]))


def video_list(request):
    latest_video = Video.objects.all().order_by('-date')
    return render(request, "gallery/video_gallery.html", {"latest_video": latest_video})


def open_tournament_registration(request):
    active_tournaments = Tournament.objects.filter(future_tournament=True)
    return render(request, "competitions/kat_competitionregistration_page.html",
                  {"active_tournaments": active_tournaments})


def tournament_registration(request):
    last_name = request.POST["last_name"]
    first_name = request.POST["first_name"]
    middle_name = request.POST["middle_name"]

    # try:
    #     participant = Participant.objects.get(last_name__iexact=last_name, first_name__iexact=first_name,
    #                                           middle_name__iexact=middle_name)
    # except Participant.DoesNotExist:
    sex = request.POST["sex"]
    birth_date = request.POST["birth_date"]
    participant = Participant(last_name=last_name, first_name=first_name, middle_name=middle_name,
                              sex=sex, birth_date=birth_date)
    participant.save()
    club = request.POST["club"]
    city = request.POST["city"]
    tournament = Participant.objects.get(tournament_title__iexact=request.POST["tournament"])
    new_tournament_registration = CompetitionRegistration(participant=participant, participant_club=club,
                                                          participant_location=city, tournament=tournament)
    new_tournament_registration.save()
    return render_to_response("kat_main_page.html", RequestContext(request))