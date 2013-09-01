# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

import api.bookmarks
import api.votes

urlpatterns = patterns('',
    url(r'^bookmarks/$', api.bookmarks.BookmarkListCreateView.as_view()),
    url(r'^bookmarks/(?P<pk>\d+)$', api.bookmarks.BookmarkDetailView.as_view()),
    url(r'^votes/$', api.votes.VoteListCreateView.as_view()),
    url(r'^votes/(?P<pk>\d+)', api.votes.VoteDetailView.as_view()),
)