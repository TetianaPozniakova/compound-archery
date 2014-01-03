# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'CalendarEvent.event_start_date'
        db.alter_column(u'kat_main_site_calendarevent', 'event_start_date', self.gf('django.db.models.fields.DateField')())

        # Changing field 'CalendarEvent.event_end_date'
        db.alter_column(u'kat_main_site_calendarevent', 'event_end_date', self.gf('django.db.models.fields.DateField')())

    def backwards(self, orm):

        # Changing field 'CalendarEvent.event_start_date'
        db.alter_column(u'kat_main_site_calendarevent', 'event_start_date', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'CalendarEvent.event_end_date'
        db.alter_column(u'kat_main_site_calendarevent', 'event_end_date', self.gf('django.db.models.fields.DateTimeField')())

    models = {
        u'kat_main_site.article': {
            'Meta': {'ordering': "('-article_publish_date',)", 'object_name': 'Article'},
            'article_abstract': ('django.db.models.fields.TextField', [], {}),
            'article_body': ('tinymce.models.HTMLField', [], {'default': "''"}),
            'article_publish_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'article_slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'article_title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'kat_main_site.calendarevent': {
            'Meta': {'object_name': 'CalendarEvent'},
            'event_end_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'event_start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'event_title': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'kat_main_site.competitionregistration': {
            'Meta': {'object_name': 'CompetitionRegistration'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['kat_main_site.Participant']"}),
            'participant_club': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'participant_location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tournament': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['kat_main_site.Tournament']"})
        },
        u'kat_main_site.participant': {
            'Meta': {'object_name': 'Participant'},
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'kat_main_site.tournament': {
            'Meta': {'object_name': 'Tournament'},
            'future_tournament': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participants_list': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['kat_main_site.Participant']", 'null': 'True', 'blank': 'True'}),
            'tournament_title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'kat_main_site.video': {
            'Meta': {'object_name': 'Video'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'video_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'video_title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['kat_main_site']