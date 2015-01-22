from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponseRedirect

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cgi_bin.urls', namespace="cgi-bin")),
)

