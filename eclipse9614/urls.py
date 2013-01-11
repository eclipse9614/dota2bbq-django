from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('dota2bbq.urls')),
    url(r'^manager/', include('manager.urls')),
    url(r'^feed/', include('feed.urls')),
)

