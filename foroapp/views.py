# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


# Create your views here.
def foroHome(request):
    return render(request, 'foroapp/foro_home.html')
