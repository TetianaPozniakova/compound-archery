from django.db import models
from inline_media.fields import TextFieldWithInlines
from datetime import datetime
from django.core.urlresolvers import reverse


class PublicManager(models.Manager):
    """Returns published articles that are not in the future."""

    def published(self):
        return self.get_query_set().filter(article_publish_date__lte=datetime.now())


class Article(models.Model):
    article_title = models.CharField(max_length=200)
    article_slug = models.SlugField(unique_for_date='article_publish_date')
    article_abstract = models.TextField()
    article_body = TextFieldWithInlines()
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