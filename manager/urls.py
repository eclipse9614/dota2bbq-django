from django.conf.urls import patterns, url

urlpatterns = patterns("manager.views",
    url(r"^$", "manage"),
    url(r"^hero_create/$", "hero_create"),
    url(r"^hero_edit/(?P<hero_name>[\w '-]+)/$", "hero_edit"),
    url(r"^hero_delete/(?P<hero_name>[\w '-]+)/$", "hero_delete"),
    url(r"^skill_edit/(?P<hero_name>[\w '-]+)/$", "skill_edit"),
    url(r"^skillbuild_edit/(?P<hero_name>[\w '-]+)/$", "skillbuild_edit"),
    url(r"^item_create/$", "item_create"),
    url(r"^item_edit/(?P<item_name>[\w '-]+)/$", "item_edit"),
    url(r"^item_delete/(?P<item_name>[\w '-]+)/$", "item_delete"),
)
