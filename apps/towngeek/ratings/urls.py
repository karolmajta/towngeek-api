# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

import api.votes

urlpatterns = patterns('',
    url(r'^votes/$', api.votes.VoteListCreateView.as_view()),
    url(r'^votes/(?P<pk>\d+)', api.votes.VoteDetailView.as_view()),
)
