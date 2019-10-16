from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^foro2/$', views.foroHome, name='foroHome'),
]