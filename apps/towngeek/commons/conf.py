# -*- coding: utf-8 -*-
from django.conf import settings as real_settings


class TgSettings(object):

    def __getattr__(self, name):
        return real_settings.TOWNGEEK[name]


settings = TgSettings()