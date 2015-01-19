from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from cgi_bin import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^bottom/$', views.bottom, name='bottom'),
    url(r'^bottom2/$', views.bottom2, name='bottom2'),
    url(r'^branches/$', views.branches, name='branches'),
    url(r'^account/$', login_required(views.account), name='account'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'cgi_bin/not-logged-in.html'}, name='login'),
)
