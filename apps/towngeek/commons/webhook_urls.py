# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

import webhooks


urlpatterns = patterns('',
    url(
        r'^mandrill/bounce/b36afb49-692d-4c4a-ab67-1d77568b40e9/$',
        webhooks.OnMandrillBounce.as_view()
    ),
)