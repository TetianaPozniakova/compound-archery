__author__ = 'noctule'
from kat_main_site.models import Article, CalendarEvent
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

admin.site.register(Article, ArticleAdmin)
admin.site.register(CalendarEvent, CalendarEventAdmin)
