__author__ = 'noctule'
from kat_main_site.models import Article
#admin.site.register()

from django.contrib import admin
from inline_media.admin import AdminTextFieldWithInlinesMixin


class ArticleAdmin(AdminTextFieldWithInlinesMixin, admin.ModelAdmin):
    list_display  = ('article_title', 'article_publish_date')
    list_filter   = ('article_publish_date',)
    search_fields = ('article_title', 'article_abstract', 'article_body')
    prepopulated_fields = {'article_slug': ('article_title',)}
    fieldsets = ((None,
                  {'fields': ('article_title', 'article_slug', 'article_abstract', 'article_body',
                              'article_publish_date',)}),)

admin.site.register(Article, ArticleAdmin)