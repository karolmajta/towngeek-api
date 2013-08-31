# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

import api.cities

urlpatterns = patterns('',
    url(r'^cities/$', api.cities.CityListView.as_view()),
    url(r'^cities/(?P<pk>\d+)', api.cities.CityDetailView.as_view()),
)
