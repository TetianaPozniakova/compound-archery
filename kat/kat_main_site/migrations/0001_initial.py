# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table(u'kat_main_site_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('article_title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('article_slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('article_abstract', self.gf('django.db.models.fields.TextField')()),
            ('article_body', self.gf('tinymce.models.HTMLField')(default='')),
            ('article_publish_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'kat_main_site', ['Article'])

        # Adding model 'CalendarEvent'
        db.create_table(u'kat_main_site_calendarevent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event_title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('event_start_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('event_end_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'kat_main_site', ['CalendarEvent'])

        # Adding model 'Video'
        db.create_table(u'kat_main_site_video', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('video_title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('video_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'kat_main_site', ['Video'])

        # Adding model 'Participant'
        db.create_table(u'kat_main_site_participant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('birth_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'kat_main_site', ['Participant'])

        # Adding model 'CompetitionRegistration'
        db.create_table(u'kat_main_site_competitionregistration', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('participant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['kat_main_site.Participant'])),
            ('participant_club', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('participant_location', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('tournament', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['kat_main_site.Tournament'])),
        ))
        db.send_create_signal(u'kat_main_site', ['CompetitionRegistration'])

        # Adding model 'Tournament'
        db.create_table(u'kat_main_site_tournament', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tournament_title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('future_tournament', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'kat_main_site', ['Tournament'])

        # Adding M2M table for field participants_list on 'Tournament'
        m2m_table_name = db.shorten_name(u'kat_main_site_tournament_participants_list')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tournament', models.ForeignKey(orm[u'kat_main_site.tournament'], null=False)),
            ('participant', models.ForeignKey(orm[u'kat_main_site.participant'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tournament_id', 'participant_id'])


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table(u'kat_main_site_article')

        # Deleting model 'CalendarEvent'
        db.delete_table(u'kat_main_site_calendarevent')

        # Deleting model 'Video'
        db.delete_table(u'kat_main_site_video')

        # Deleting model 'Participant'
        db.delete_table(u'kat_main_site_participant')

        # Deleting model 'CompetitionRegistration'
        db.delete_table(u'kat_main_site_competitionregistration')

        # Deleting model 'Tournament'
        db.delete_table(u'kat_main_site_tournament')

        # Removing M2M table for field participants_list on 'Tournament'
        db.delete_table(db.shorten_name(u'kat_main_site_tournament_participants_list'))


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
            'event_end_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'event_start_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
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