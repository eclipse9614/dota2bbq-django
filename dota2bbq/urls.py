from django.conf.urls import patterns, url

urlpatterns = patterns('dota2bbq.views',
    url(r'^$', 'index'),
    url(r'^heroes/$', 'heroes'),
    url(r'^items/$', 'items'),
    url(r'^hero/(?P<hero_name>[\w ]+)/$', 'hero'),
    url(r'^signin/$', 'signin'),
    url(r'^signoff/$', 'signoff'),
    url(r'^ajax/combined/$', 'combined_feed'),
    url(r'^ajax/items/$', 'items_feed'),
)
