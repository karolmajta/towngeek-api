# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save, post_delete

import towngeek.commons.tasks


class CountUpdater(object):

    def __init__(self, foreign_key, source, to, dt=0):
        self.foreign_key = foreign_key
        self.source = source
        self.to = to
        self.countdown = dt

    def __call__(self, sender, **kwargs):
        instance = kwargs['instance']
        try:
            target = getattr(instance, self.foreign_key)
        except ObjectDoesNotExist:
            target = None
        if target is None:
            return
        ct = ContentType.objects.get_for_model(
            target,
            for_concrete_model=False
        )
        towngeek.commons.tasks.count.apply_async(
            [ct.app_label,
            ct.model,
            target.pk,
            self.source,
            self.to],
            countdown=self.countdown
        )


class AggrUpdater(object):

    def __init__(self, foreign_key, source, field, to, aggr, empty=None, dt=0):
        self.foreign_key = foreign_key
        self.source = source
        self.field = field
        self.to = to
        self.aggregation = aggr
        self.empty = empty
        self.countdown = dt

    def __call__(self, sender, **kwargs):
        instance = kwargs['instance']
        try:
            target = getattr(instance, self.foreign_key)
        except ObjectDoesNotExist:
            target = None
        if target is None:
            return
        ct = ContentType.objects.get_for_model(
            target,
            for_concrete_model=False
        )
        towngeek.commons.tasks.aggregate.apply_async(
            [ct.app_label,
            ct.model,
            target.pk,
            self.source,
            self.field,
            self.to,
            self.aggregation],
            empty=self.empty,
            countdown=self.countdown
        )


class track(object):

    @staticmethod
    def count(sender, foreign_key, source, to, dt=0):
        updater = CountUpdater(foreign_key, source, to, dt=dt)
        post_save.connect(updater, sender=sender, weak=False)
        post_delete.connect(updater, sender=sender, weak=False)

    @staticmethod
    def aggregation(
            sender,
            foreign_key,
            source,
            field,
            to,
            aggregation,
            empty,
            dt=0
        ):
        updater = AggrUpdater(
            foreign_key,
            source,
            field,
            to,
            aggregation,
            empty=empty,
            dt=dt
        )
        post_save.connect(updater, sender=sender, weak=False)
        post_delete.connect(updater, sender=sender, weak=False)