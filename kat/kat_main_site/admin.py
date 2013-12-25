__author__ = 'noctule'
from models import Article, CalendarEvent, Participant, CompetitionRegistration, Tournament
#admin.site.register()

from django.contrib import admin


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_title', 'article_publish_date')
    list_filter = ('article_publish_date',)
    search_fields = ('article_title', 'article_abstract', 'article_body')
    prepopulated_fields = {'article_slug': ('article_title',)}
    fieldsets = ((None,
                  {'fields': ('article_title', 'article_slug', 'article_abstract', 'article_body',
                              'article_publish_date',)}),)


class CalendarEventAdmin(admin.ModelAdmin):
    list_display = ["event_title", "event_start_date", "event_end_date"]
    list_filter = ["event_start_date"]


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ["last_name", "first_name", "middle_name"]


class CompetitionRegistrationAdmin(admin.ModelAdmin):
    list_display = ["tournament", "participant", "participant_club"]
    list_filter = ["tournament"]


class TournamentAdmin(admin.ModelAdmin):
    list_display = ["tournament_title"]


admin.site.register(Article, ArticleAdmin)
admin.site.register(CalendarEvent, CalendarEventAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(CompetitionRegistration, CompetitionRegistrationAdmin)
admin.site.register(Tournament, TournamentAdmin)
