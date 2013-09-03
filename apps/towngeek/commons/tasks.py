# -*- coding: utf-8 -*-
import celery

import towngeek.commons.aggregations as aggr
import towngeek.commons.mailing as mailing


@celery.task
def aggregate(*args, **kwargs):
    aggr.aggregate(*args, **kwargs)


@celery.task
def count(*args, **kwargs):
    aggr.count(*args, **kwargs)


@celery.task
def send_mail(*args, **kwargs):
    mailing.send_email(*args, **kwargs)


@celery.task
def deactivate_for_emails(*args, **kwargs):
    mailing.deactivate_for_emails(*args, **kwargs)