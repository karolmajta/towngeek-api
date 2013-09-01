# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes.models import ContentType

Count = "COUNT"
Min = "MIN"
Max = "MAX"
Sum = "SUM"
Avg = "AVG"
StdDev = "STDEV"
Variance = "VARIANCE"

AGGREGATIONS = {
    Count: models.Count,
    Min: models.Min,
    Max: models.Max,
    Sum: models.Sum,
    Avg: models.Avg,
    StdDev: models.StdDev,
    Variance: models.Variance,
}


def obj_or_none(app_label, model, pk):
    ct = ContentType.objects.get(app_label=app_label, model=model)
    Model = ct.model_class()
    try:
        return Model.objects.get(pk=pk)
    except Model.DoesNotExist:
        return None


def aggregate(app_label, model, pk, source, field, to, aggregation, empty=None):
    obj = obj_or_none(app_label, model, pk)
    if obj:
        related = getattr(obj, source)
        aggr_dict = related.all().aggregate(r=AGGREGATIONS[aggregation](field))
        result = aggr_dict['r']
        setattr(obj, to, result if result else empty)
        obj.save()


def count(app_label, model, pk, source, to):
    obj = obj_or_none(app_label, model, pk)
    if obj:
        related = getattr(obj, source)
        setattr(obj, to, related.count())
        obj.save()