from django.db import models


class City(models.Model):

    name = models.CharField(max_length=511)
    latitude = models.DecimalField(decimal_places=9, max_digits=11)
    longitude = models.DecimalField(decimal_places=9, max_digits=12)

    def __unicode__(self):
        return self.name