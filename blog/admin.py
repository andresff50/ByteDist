# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import Category, Tag, Post

# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "created_date", "published_date", "author", "c_view", "status"]
    list_filter = ["created_date", "published_date", "status"]
    search_fields = ["title", "content"]
    prepopulated_fields = {'slug': ('title',)}
    #readonly_fields = ['slug']
    #date_hierarchy = 'published_date'
    #ordering = ['status', 'published_date']

    class Meta:
        model = Post

class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ["title","orden"]
    search_fields = ["title"]
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = Category


class TagModelAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]

    class Meta:
        model = Tag



admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Tag, TagModelAdmin)
admin.site.register(Post, PostModelAdmin)