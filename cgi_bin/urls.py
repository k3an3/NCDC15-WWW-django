from django.conf.urls import patterns, url

from cgi_bin import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^bottom/$', views.bottom, name='bottom'),
)
