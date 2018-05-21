from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page,name='article_page'),
    url(r'^edit/$', views.edit_page,name='edit_page'),
    url(r'^edit/action$', views.edit_action,name='edit_action'),
    url(r'^update/(?P<article_id>[0-9]+)$', views.update_article, name='update_article'),
    url(r'^update/action/(?P<article_id>[0-9]+)$', views.update_action, name='update_action'),
]
