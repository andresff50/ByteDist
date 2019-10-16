# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactForm
from django.contrib import messages
from blog.models import Category

from django.core.mail import send_mail
from django.conf import settings


def indexInformation(request):
    categories = Category.objects.all().order_by('orden')
    return render(request, 'informationapp/indexInformation.html', {'categories' : categories})

def informacion(request):
    categories = Category.objects.all().order_by('orden')
    return render(request, 'informationapp/informacion.html', {'categories' : categories})

def contacto(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            subject = request.POST.get('subject', '')
            message = request.POST.get('message', '')
            contenido_mensaje = "Este mensaje lo envio: " + name + "\n" + "Correo electronico: " + email + "\n" + "Mensaje:" + message
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [settings.EMAIL_HOST_USER]
            send_mail(subject, contenido_mensaje, email_from, recipient_list )
            form = ContactForm()
            return HttpResponseRedirect('?submitted')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    
    categories = Category.objects.all().order_by('orden')
    return render(request, 'informationapp/contacto.html', { 'categories' : categories, 'form': form, 'submitted': submitted })

def publicidad(request):
    categories = Category.objects.all().order_by('orden')
    return render(request, 'informationapp/publicidad.html', {'categories' : categories})

def politicas(request):
    categories = Category.objects.all().order_by('orden')
    return render(request, 'informationapp/paginaPoliticas.html', {'categories' : categories})


