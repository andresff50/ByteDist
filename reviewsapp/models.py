# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from django.db.models import permalink
from django.core.urlresolvers import reverse
from django.utils.encoding import smart_str, smart_unicode
from django.utils.text import slugify

from django.db import models
from blog.models import Tag, PublishedManager



# Create your models here.

class Review(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True)
    tags = models.ManyToManyField(Tag)
    content = RichTextUploadingField()
    resumen = models.CharField(max_length=150)
    # identify when post was created
    created_date = models.DateTimeField(editable=False, default=timezone.now)
    # set publish date initially to blank and null as drafts are allowed
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    # record how ofter a post is seen
    c_view = models.IntegerField(default=0)
    image1 = models.ImageField(upload_to="images/postimg", blank=True, null=True)
    image2 = models.ImageField(upload_to="images/postimg", blank=True, null=True)
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
        super(Review, self).save()

    # permalink deocrator is used to reverse the URL for a particular object'''
    @permalink
    def get_review_detail_detail_url(self):
        return ('review_detail', [self.slug])
