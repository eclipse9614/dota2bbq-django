from django.conf.urls import patterns, url

urlpatterns = patterns("dota2bbq.views",
    url(r"^$", "index"),
    url(r"^heroes/$", "heroes"),
    url(r"^items/$", "items"),
    url(r"^community/$", "community"),
    url(r"^hero/(?P<hero_name>[\w '-]+)/$", "hero"),
    url(r"^signin/$", "signin"),
    url(r"^signoff/$", "signoff"),
)
