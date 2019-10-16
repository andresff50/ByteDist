# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.db.models import permalink
from django.core.urlresolvers import reverse
from django.utils.encoding import smart_str, smart_unicode
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from blog.models import Tag, PublishedManager
from django.db import models

# Create your models here.
class News_video(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True)
    tags = models.ManyToManyField(Tag)
    video_url = models.CharField(max_length=400)
    thumbnail = models.ImageField(upload_to="images/thumbnailvideos", blank=True, null=True)
    content = RichTextUploadingField()
    # identify when post was created
    created_date = models.DateTimeField(editable=False, default=timezone.now)
    # set publish date initially to blank and null as drafts are allowed
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    c_view = models.IntegerField(default=0)
    STATUS_CHOICES = (
      ('draft', 'Draft'),
      ('published', 'Published')
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager() # the default manager
    published_objects = PublishedManager() # The publish-specific manager.

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_slug(self):
        slug = slugify(self.title)
        return slug

    def save(self, *args, **kwargs):
        self.title = smart_unicode(self.title)
        self.slug = self.get_slug()
        super(News_video, self).save()

    @permalink
    def get_video_detail_url(self):
        return ('video_detail', [self.slug])
