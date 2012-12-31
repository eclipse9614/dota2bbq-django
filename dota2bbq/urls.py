from django.conf.urls import patterns, url

urlpatterns = patterns('dota2bbq.views',
    url(r'^$', 'index'),
)
