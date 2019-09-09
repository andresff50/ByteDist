from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^galeria/$', views.videoslist, name='videoslist'),
    url(r'^detalle/(?P<slug>[-\w]+)/$', views.video_detail, name='video_detail'),
]