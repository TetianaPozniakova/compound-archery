# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from kat import settings as news_settings
from django.core.validators import MaxLengthValidator
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager

try:
    from south.modelsinspector import add_introspection_rules
except ImportError:
    pass

try:
    from tinymce.models import HTMLField
except ImportError:
    from django.db.models.fields import TextField as HTMLField


MONTHS = [
    _(' January'), _(' February'), _(' March'), _(' April'), _(' May'),
    _(' June'), _(' July'), _(' August'), _(' September'), _(' October'),
    _(' November'), _(' December')
]


class News(models.Model):
    class Meta:
        verbose_name = u'Новость'
        verbose_name_plural = u'Новости'
        ordering = ['-date', 'title', ]

    title = models.CharField(max_length=500, verbose_name=u'Заголовок новости')
    slug = models.SlugField(max_length=200, verbose_name=u'Слаг', unique_for_date='date')

    date = models.DateTimeField(verbose_name=u'Дата', default=datetime.datetime.now)

    short = HTMLField(validators=[MaxLengthValidator(1400)], verbose_name=u'Кратное описание', default='', blank=True)
    text = HTMLField(validators=[MaxLengthValidator(50000)], verbose_name=u'Полный текст', default='', blank=True)

    show = models.BooleanField(verbose_name=u'Опубликовано', default=True)

    tags = TaggableManager()

    def month(self):
        return MONTHS[self.date.month - 1]

    def save(self, *args, **kwds):
        need_update = False
        if self.slug is None:
            if self.id is None:
                need_update = True
                self.slug = ''
            else:
                self.slug = self.id
        super(News, self).save(*args, **kwds)
        if need_update:
            self.slug = self.id
            super(News, self).save(force_update=True)
    save.alters_data = True

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={
            'year': '%04d' % self.date.year,
            'month': '%02d' % self.date.month,
            'day': '%02d' % self.date.day,
            'slug': self.slug,
        })

    def __unicode__(self):
        return self.title

try:
    add_introspection_rules([], ['tinymce\.models\.HTMLField'])
except:
    pass
