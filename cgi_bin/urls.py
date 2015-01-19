from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from cgi_bin import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^bottom/$', views.bottom, name='bottom'),
    url(r'^bottom2/$', views.bottom2, name='bottom2'),
    url(r'^branches/$', views.branches, name='branches'),
    url(r'^landing/$', login_required(views.landing), name='landing'),
    url(r'^landing/show_user/$', login_required(views.show_user), name='show_user'),
    url(r'^landing/make_payment/$', login_required(views.make_payment), name='make_payment'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'cgi_bin/not-logged-in.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'cgi-bin:login'}, name='logout'),
)
