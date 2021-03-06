# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from kat_news.models import News
from kat import settings as news_settings
if news_settings.NEWS_TAGGING:
    from taggit.forms import TagField


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
    title = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), max_length=500)
    if news_settings.NEWS_TAGGING:
        tags = TagField(required=False)


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'show', ]
    prepopulated_fields = {'slug': ('title',)}
    form = NewsForm

try:
    admin.site.register(News, NewsAdmin)
except admin.sites.AlreadyRegistered:
    pass
