# coding=utf-8
from django.conf.urls import patterns, url, include
from views import indexView

urlpatterns = patterns('',
    url(r'^$', indexView.as_view(), name='index'),
)