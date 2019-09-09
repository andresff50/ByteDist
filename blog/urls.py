from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.get_index, name='index'),
    url(r'^noticias/$', views.post_list, name='post_list'),
    url(r'^filterpage/', views.search_page, name='search_page'),
    url(r'^(?P<slug>[-\w]+)/$', views.postByCategory, name='postByCategory'),
    url(r'^noticias/(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail'),
    #([0-9]+)
]