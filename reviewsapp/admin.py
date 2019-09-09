# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Review
# Register your models here.
class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ["title", "created_date", "published_date", "author", "c_view", "status"]
    list_filter = ["created_date", "published_date", "status"]
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ["title"]

    class Meta:
        model = Review


admin.site.register(Review, ReviewModelAdmin)