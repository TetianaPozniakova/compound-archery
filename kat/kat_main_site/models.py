 # -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse
from django.core.validators import MaxLengthValidator
from django.forms import ModelForm

try:
    from tinymce.models import HTMLField
except ImportError:
    from django.db.models.fields import TextField as HTMLField


class PublicManager(models.Manager):
    """Returns published articles that are not in the future."""

    def published(self):
        return self.get_query_set().filter(article_publish_date__lte=datetime.now())


class Article(models.Model):
    article_title = models.CharField(max_length=200)
    article_slug = models.SlugField(unique_for_date='article_publish_date')
    article_abstract = models.TextField()
    article_body = HTMLField(validators=[MaxLengthValidator(14000)], default='', blank=False)
    article_publish_date = models.DateTimeField(default=datetime.now)

    objects = PublicManager()

    class Meta:
        ordering = ('-article_publish_date',)

    def __unicode__(self):
        return self.article_title

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'year': self.article_publish_date.year,
                 'month': int(self.article_publish_date.strftime('%m').lower()),
                 'day': self.article_publish_date.day,
                 'slug': self.article_slug})


class CalendarEvent(models.Model):
    event_title = models.CharField(max_length=150)
    event_start_date = models.DateTimeField(default=datetime.now)
    event_end_date = models.DateTimeField(default=datetime.now)
    #TODO: add choice field to select type of the competition in order to color cells on the calendar

    def __unicode__(self):
        return "%s: from %s to %s" % (self.event_title, self.event_start_date, self.event_end_date)


class Video(models.Model):
    video_title = models.CharField(max_length=150)
    video_id = models.CharField(max_length=50)
    date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.video_title


class Participant(models.Model):
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    middle_name = models.CharField(max_length=50, verbose_name="Отчество")
    sex = models.CharField(max_length=1, choices=(('M', 'Мужской'), ('F', 'Женский')), verbose_name="Пол")
    birth_date = models.DateField(verbose_name="Дата рождения")

    def __unicode__(self):
        return "%s %s %s" % (self.last_name, self.first_name, self.middle_name)


class CompetitionRegistration(models.Model):
    participant = models.ForeignKey('Participant')
    participant_club = models.CharField(max_length=50, verbose_name="Спортивное общество")
    participant_location = models.CharField(max_length=50, verbose_name="Место проживания")
    tournament = models.ForeignKey('Tournament')

    def __unicode__(self):
        return "%s %s (%s)" % (self.participant.last_name, self.participant.first_name, self.tournament.tournament_title)


class Tournament(models.Model):
    tournament_title = models.CharField(max_length=150)
    participants_list = models.ManyToManyField(Participant, blank=True, null=True)
    future_tournament = models.BooleanField(default=True)

    def __unicode__(self):
        return self.tournament_title


class ParticipantForm(ModelForm):
    class Meta:
        model = Participant


class CompetitionRegistrationForm(ModelForm):
    class Meta:
        model = CompetitionRegistration
        fields = ['participant_club', 'participant_location']