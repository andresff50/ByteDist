# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.utils import timezone
from django.db.models import permalink
from django.core.urlresolvers import reverse
from django.utils.encoding import smart_str, smart_unicode
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField

from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50)
    orden = models.IntegerField(default=0)
    slug = models.SlugField(max_length=50, unique=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_slug(self):
        slug = slugify(self.title)
        return slug

    def save(self, *args, **kwargs):
        self.slug = self.get_slug()
        super(Category, self).save()

    # permalink deocrator is used to reverse the URL for a particular object'''
    @permalink
    def get_category_url(self):
        return ('postByCategory', [self.slug])
        

class Tag(models.Model):
    title = models.CharField(max_length=40, default='')

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class PublishedManager(models.Manager):
    def get_queryset(self):
        #'''select only published posts'''
        return super(PublishedManager, self).get_queryset().filter(status="published")


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True)
    colorhexa = models.CharField(max_length=8,blank=True, null=True)
    content = RichTextUploadingField()
    resumen = models.CharField(max_length=150)
    # identify when post was created
    created_date = models.DateTimeField(editable=False, default=timezone.now)
    # set publish date initially to blank and null as drafts are allowed
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    # record how ofter a post is seen
    c_view = models.IntegerField(default=0)
    # tags field
    tags = models.ManyToManyField(Tag)
    # add images to a post #stores relative path to image
    imageslider = models.ImageField(upload_to="images/postimg", blank=True, null=True)
    image1 = models.ImageField(upload_to="images/postimg", blank=True, null=True)
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
        super(Post, self).save()

    # permalink deocrator is used to reverse the URL for a particular object'''
    @permalink
    def get_post_detail_url(self):
        return ('post_detail', [self.slug])