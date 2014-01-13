# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import TemplateView, ListView, DateDetailView
from models import Participant, CompetitionRegistration, Tournament, ParticipantForm, CompetitionRegistrationForm
from models import Article, CalendarEvent, Video
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
        if change == "next":
            mod = mdelta
        elif change == "prev":
            mod = -mdelta

        year, month = (now + mod).timetuple()[:2]

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
            day_date = date(year, month, day)
            entries = CalendarEvent.objects.filter(event_start_date__lte=day_date, event_end_date__gte=day_date)
            if day == nday and year == nyear and month == nmonth:
                current = True

        lst[week].append((day, entries, current))
        if len(lst[week]) == 7:
            lst.append([])
            week += 1

    return render_to_response("calendar/kat_calendar_month_view.html", dict(year=year, month=month,
                                                                            month_days=lst, mname=mnames[month - 1]))


def main(request, year=None):
    """Main listing, years and months; three years per page."""
    # prev / next years
    if year:
        year = int(year)
    else:
        year = time.localtime()[0]

    nowy, nowm = time.localtime()[:2]
    lst = []

    # create a list of months for each year, indicating ones that contain entries and current
    for y in [year, year + 1, year + 2]:
        mlst = []
        for n, month in enumerate(mnames):
            entry = current = False # are there entry(s) for this month; current month?
            entries = CalendarEvent.objects.filter(event_start_date__year=y, event_start_date__month=n + 1)

            if entries:
                entry = True
            if y == nowy and n + 1 == nowm:
                current = True
            mlst.append(dict(n=n + 1, name=month, entry=entry, current=current))
        lst.append((y, mlst))

    return render_to_response("calendar/kat_calendar_page.html", dict(years=lst, year=year),
                              context_instance=RequestContext(request))


def video_list(request):
    latest_video = Video.objects.all().order_by('-date')
    return render(request, "gallery/video_gallery.html", {"latest_video": latest_video})


def participants_lists(request):
    active_tournaments = Tournament.objects.filter(future_tournament=True)
    return render(request, "competitions/kat_registered_participant_page.html",
                  {"active_tournaments": active_tournaments})


def tournament_registration(request):
    if request.method == 'POST':  # If the form has been submitted...
        pform = ParticipantForm(request.POST)  # A form bound to the POST data
        rform = CompetitionRegistrationForm(request.POST)
        tournament = Tournament.objects.get(tournament_title__iexact=request.POST["tournament"])
        if pform.is_valid() and rform.is_valid():  # All validation rules pass
            last_name = request.POST["last_name"]
            first_name = request.POST["first_name"]
            middle_name = request.POST["middle_name"]
            try:
                participant = Participant.objects.get(last_name__iexact=last_name, first_name__iexact=first_name,
                                                      middle_name__iexact=middle_name)
            except Participant.DoesNotExist:
                participant = pform.save()
            new_tournament_registration = rform.save(commit=False)
            new_tournament_registration.participant = participant
            new_tournament_registration.tournament = tournament
            new_tournament_registration.save()
            tournament.participants_list.add(participant)
            return HttpResponseRedirect('/participants-lists/')  # Redirect after POST
    else:
        pform = ParticipantForm()
        rform = CompetitionRegistrationForm()
    active_tournaments = Tournament.objects.filter(future_tournament=True)
    return render(request, "competitions/kat_competitionregistration_page.html",
                  {"pform": pform, "rform": rform, "active_tournaments": active_tournaments})

    # def tournament_registration(request):
    #     last_name = request.POST["last_name"]
    #     first_name = request.POST["first_name"]
    #     middle_name = request.POST["middle_name"]
    #
    #     # try:
    #     #     participant = Participant.objects.get(last_name__iexact=last_name, first_name__iexact=first_name,
    #     #                                           middle_name__iexact=middle_name)
    #     # except Participant.DoesNotExist:
    #     sex = request.POST["sex"]
    #     birth_date = request.POST["birth_date"]
    #     participant = Participant(last_name=last_name, first_name=first_name, middle_name=middle_name,
    #                               sex=sex, birth_date=birth_date)
    #     participant.save()
    #     club = request.POST["club"]
    #     city = request.POST["city"]
    #     tournament = Tournament.objects.get(tournament_title__iexact=request.POST["tournament"])
    #     new_tournament_registration = CompetitionRegistration(participant=participant, participant_club=club,
    #                                                           participant_location=city, tournament=tournament)
    #     new_tournament_registration.save()
    #     return render_to_response("kat_main_page.html", RequestContext(request))