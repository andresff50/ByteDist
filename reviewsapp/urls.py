from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^galeria/$', views.reviewsList, name='reviewsList'),
    url(r'^detalle/(?P<slug>[-\w]+)/$', views.review_detail, name='review_detail'),
]