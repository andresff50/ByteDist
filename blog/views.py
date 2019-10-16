# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.utils.encoding import smart_str, smart_unicode
from .models import Category, Post
from mvideo.models import News_video

# Create your views here.
def post_list(request):
    # Get all published posts
    posts_all = Post.published_objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    new_posts = Post.published_objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:3]
    # set up pagination (6 posts per page)
    paginator = Paginator(posts_all, 16)
    page = request.GET.get('page')
    categories = Category.objects.all().order_by('orden')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # if page is out of range, deliver last page of results
        posts = paginator.page(paginator.mum_pages)

    return render(request, 'blog/post_list.html', {
        'page' : page,
        'posts' : posts,
        'categories' : categories,
        'new_posts' : new_posts,
        })


def post_detail(request, slug):
    new_posts = Post.published_objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:3]
    post_similares = Post.published_objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:2]
    post = get_object_or_404(Post, slug=slug, status='published')
    categories = Category.objects.all().order_by('orden')
    if post.status=='published':
        post.c_view += 1 # clock up the number of post views
        post.save()
    return render(request, 'blog/post_detail.html', {
            'new_posts' : new_posts,
            'post' : post,
            'categories' : categories,
            'post_similares' : post_similares,
            })

def postByCategory(request, slug):
        new_posts = Post.published_objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:3]
        categoriObject = get_object_or_404(Category, slug=slug)
        posts_by_category = Post.published_objects.filter(categories__slug=slug, published_date__lte=timezone.now()).order_by('-published_date')
        # set up pagination (6 posts per page)
        paginator = Paginator(posts_by_category, 16)
        page = request.GET.get('page')
        categories = Category.objects.all().order_by('orden')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            posts = paginator.page(1)
        except EmptyPage:
            #if page is out of range, deliver last page of results
            posts = paginator.page(paginator.mum_pages)
        return render (request, 'blog/category_post.html', {
            'new_posts' : new_posts,
            'page' : page,
            'posts' : posts,
            #'posts_by_category' : posts_by_category,
            'categories' : categories,
            'categoriObject' : categoriObject,
            })

# Home view
def get_index(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    new_posts = Post.published_objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:3]
    postslider = Post.published_objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:5]
    posttop4 = Post.published_objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:6]
    videostop4 = News_video.published_objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:4]
    # Get all published posts
    posts_all = Post.published_objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    # set up pagination (6 posts per page)
    paginator = Paginator(posts_all, 12)
    page = request.GET.get('page')
    categories = Category.objects.all().order_by('orden')


    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # if page is out of range, deliver last page of results
        posts = paginator.page(paginator.mum_pages)
    return render(request, 'blog/index.html', {
        'new_posts' : new_posts,
        'postslider' : postslider,
        'page' : page,
        'posts': posts,
        'categories': categories,
        'posttop4': posttop4,
        'videostop4' : videostop4,

        })
def search_page(request):
    new_posts = Post.published_objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:3]
    posts_all = Post.published_objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    #videos_news = News_video.published_objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    videos_all = News_video.published_objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    categories = Category.objects.all().order_by('orden')

    query = request.GET.get("q")
    if query:
        posts_all = posts_all.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__title__icontains=query) |
            Q(author__username__icontains=query)
            ).distinct()[:40]
        videos_all = videos_all.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__title__icontains=query) |
            Q(author__username__icontains=query)
            ).distinct()[:40]

    return render(request, 'blog/search_page.html', {
        'new_posts' : new_posts,
        'posts_all' : posts_all,
        'videos_all' : videos_all,
        'categories': categories,
    })