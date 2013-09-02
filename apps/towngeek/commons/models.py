# -*- coding: utf-8 -*-
"""
This module is here only to allow towngeek.commons to be added
to INSTALLED_APPS and run its migrations, and to register signal
hooks for User model.
"""

from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
User = get_user_model()

import towngeek.commons.tasks as tasks


def on_user_save(*args, **kwargs):
    print "user_on_save"
    user = kwargs['instance']
    created = kwargs['created']
    if created:
        tasks.send_mail.delay(
            'hello@towngeek.pl',
            user.email,
            'Welcome to Towngeek!',
            'welcome',
            {
                'full_name': u"{0} {1}".format(user.first_name, user.last_name),
                'username': user.username
            }
        )

post_save.connect(on_user_save, sender=User)