# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.utils.encoding import smart_str, smart_unicode
from .models import News_video
from blog.models import Category, Post

from django.shortcuts import render

# Create your views here.

def videoslist(request):
    posttop4 = Post.published_objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:8]
    new_posts = Post.published_objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:3]
    videos_news_all = News_video.published_objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    paginator = Paginator(videos_news_all, 8)
    page = request.GET.get('page')
    categories = Category.objects.all().order_by('orden')
    
    try:
        videos_news = paginator.page(page)
    except PageNotAnInteger:
        videos_news = paginator.page(1)
    except EmptyPage:
        videos_news = paginator.page(paginator.mum_pages)

    return render(request, 'mvideo/videoslist.html', {
        'page' : page,
        'videos_news': videos_news,
        'new_posts' : new_posts,
        'posttop4' : posttop4,
        'categories': categories,
    })

def video_detail(request, slug):
    videos_similares = News_video.published_objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:2]
    new_posts = Post.published_objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:3]
    videoDetail = get_object_or_404(News_video, slug=slug, status='published')
    categories = Category.objects.all().order_by('orden')

    if videoDetail.status=='published':
        videoDetail.c_view += 1 # clock up the number of post views
        videoDetail.save()
    return render(request, 'mvideo/video_detail.html', {
        'videoDetail' : videoDetail,
        'new_posts' : new_posts,
        'videos_similares' : videos_similares,
        'categories': categories,
    })