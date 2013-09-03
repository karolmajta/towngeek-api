# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

import api.users


urlpatterns = patterns('',
    url(r'^users/$', api.users.UserListCreateView.as_view()),
    url(r'^users/(?P<pk>\d+)', api.users.UserDetailView.as_view()),
)