from django.conf.urls import patterns, url

urlpatterns = patterns('dota2bbq.views',
    url(r'^$', 'index'),
    url(r'^heroes$', 'heroes'),
    url(r'^ajax/combined$', 'combined_feed'),
)
