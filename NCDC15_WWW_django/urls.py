from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponseRedirect

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'NCDC15_WWW_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', lambda r: HttpResponseRedirect('cgi-bin/')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cgi-bin/', include('cgi_bin.urls', namespace="cgi-bin")),
)

