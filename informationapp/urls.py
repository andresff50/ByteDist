from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pagelist/$', views.indexInformation, name='indexInformation'),
    url(r'^informacion/$', views.informacion, name='informacion'),
    url(r'^contacto/$', views.contacto, name='contacto'),
    url(r'^publicidad/$', views.publicidad, name='publicidad'),
    url(r'^politicas/$', views.politicas, name='politicas'),
]