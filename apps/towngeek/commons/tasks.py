# -*- coding: utf-8 -*-
import celery

import towngeek.commons.aggregations as aggr


@celery.task
def aggregate(*args, **kwargs):
    aggr.aggregate(*args, **kwargs)


@celery.task
def count(*args, **kwargs):
    aggr.count(*args, **kwargs)