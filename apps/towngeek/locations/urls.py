# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

import api.cities
import api.cityknowledges

urlpatterns = patterns('',
    url(r'^cities/$', api.cities.CityListView.as_view()),
    url(r'^cities/(?P<pk>\d+)$', api.cities.CityDetailView.as_view()),
    url(
        r'^city-knowledges/$',
        api.cityknowledges.CityKnowledgeListCreateView.as_view()
    ),
    url(
        r'^city-knowledges/(?P<pk>\d+)$',
        api.cityknowledges.CityKnowledgeDetailView.as_view()
    ),
)
