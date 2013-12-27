from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse
from django.core.validators import MaxLengthValidator

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
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), blank=True, null=True)
    birth_date = models.DateField('birth date')

    def __unicode__(self):
        return "%s %s %s" % (self.last_name, self.first_name, self.middle_name)


class CompetitionRegistration(models.Model):
    participant = models.ForeignKey('Participant')
    participant_club = models.CharField(max_length=50)
    participant_location = models.CharField(max_length=50)
    tournament = models.ForeignKey('Tournament')

    def __unicode__(self):
        return "%s %s (%s)" % (self.participant.last_name, self.participant.first_name, self.tournament.tournament_title)


class Tournament(models.Model):
    tournament_title = models.CharField(max_length=150)
    participants_list = models.ManyToManyField(Participant, blank=True, null=True)
    future_tournament = models.BooleanField(default=True)

    def __unicode__(self):
        return self.tournament_title
