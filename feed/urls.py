from django.conf.urls import patterns, url

urlpatterns = patterns("feed.views",
    url(r"^combined/$", "combined"),
    url(r"^items/$", "items"),
    url(r"^feed$", "feed"),
)
