# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseNotFound
from django.utils import timezone
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404,redirect
from django.utils.encoding import smart_str, smart_unicode
from blog.models import Category, Post
from mvideo.models import News_video
from .models import Review

# Create your views here.
def reviewsList(request):
    new_posts = Post.published_objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:3]
    Review_all = Review.published_objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    categories = Category.objects.all().order_by('orden')
    paginator = Paginator(Review_all, 12)
    page = request.GET.get('page')
    try:
        review_pag = paginator.page(page)
    except PageNotAnInteger:
        review_pag = paginator.page(1)
    except EmptyPage:
        review_pag = paginator.page(paginator.mum_pages)

    return render(request, 'reviewsapp/reviews_list.html', {
        'page' : page,
        'review_pag' : review_pag,
        'new_posts' : new_posts,
        'categories': categories,

    })

def review_detail(request, slug):
    videos_similares = News_video.published_objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:2]
    new_posts = Post.published_objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:3]
    reviewDetail = get_object_or_404(Review, slug=slug, status='published')
    categories = Category.objects.all().order_by('orden')
    if reviewDetail.status=='published':
        reviewDetail.c_view += 1 # clock up the number of post views
        reviewDetail.save()
    return render(request, 'reviewsapp/review_detail.html', {
        'reviewDetail' : reviewDetail,
        'new_posts' : new_posts,
        'videos_similares' : videos_similares,
        'categories': categories,
    })
