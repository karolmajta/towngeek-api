# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save, post_delete

from towngeek.commons.aggregations import count, aggregate


class CountUpdater(object):

    def __init__(self, foreign_key, source, to):
        self.foreign_key = foreign_key
        self.source = source
        self.to = to

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
        count(ct.app_label, ct.model, target.pk, self.source, self.to)


class AggrUpdater(object):

    def __init__(self, foreign_key, source, field, to, aggregation, empty=None):
        self.foreign_key = foreign_key
        self.source = source
        self.field = field
        self.to = to
        self.aggregation = aggregation
        self.empty = empty

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
        aggregate(
            ct.app_label,
            ct.model,
            target.pk,
            self.source,
            self.field,
            self.to,
            self.aggregation,
            empty=self.empty
        )


class track(object):

    @staticmethod
    def count(sender, foreign_key, source, to):
        updater = CountUpdater(foreign_key, source, to)
        post_save.connect(updater, sender=sender, weak=False)
        post_delete.connect(updater, sender=sender, weak=False)

    @staticmethod
    def aggregation(sender, foreign_key, source, field, to, aggregation, empty):
        updater = AggrUpdater(
            foreign_key,
            source,
            field,
            to,
            aggregation,
            empty=empty
        )
        post_save.connect(updater, sender=sender, weak=False)
        post_delete.connect(updater, sender=sender, weak=False)