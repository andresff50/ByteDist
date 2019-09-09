# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import News_video

# Register your models here.
class VideoModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ["title", "created_date", "published_date", "author", "c_view", "status"]
    search_fields = ["title"]

    class Meta:
        model = News_video


admin.site.register(News_video, VideoModelAdmin)