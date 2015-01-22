from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from cgi_bin import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^bottom/$', views.bottom, name='bottom'),
    url(r'^bottom2/$', views.bottom2, name='bottom2'),
    url(r'^branches/$', views.branches, name='branches'),
    url(r'^cgi-bin/actions/get-admin-access-token$', views.admintoken, name='admintoken'),
    url(r'^cgi-bin/show/landing/$', login_required(views.landing), name='landing'),
    url(r'^cgi-bin/show/show-user$', views.show_user, name='show_user'),
    url(r'^cgi-bin/actions/find-user$', views.find_user, name='find_user'),
    url(r'^cgi-bin/actions/create-user$', views.create_user, name='create_user'),
    url(r'^cgi-bin/actions/make-deposit$', views.make_deposit, name='make_deposit'),
    url(r'^cgi-bin/actions/make-withdrawal$', views.make_withdrawal, name='make_withdrawal'),
    url(r'^cgi-bin/actions/make-payment$', views.make_payment, name='make_payment'),
    url(r'^cgi-bin/login/$', 'django.contrib.auth.views.login', {'template_name': 'cgi_bin/not-logged-in.html'}, name='login'),
    url(r'^cgi-bin/logout/$', 'django.contrib.auth.views.logout', {'next_page': 'cgi-bin:login'}, name='logout'),
)
