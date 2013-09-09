from django.contrib.auth import get_user_model
User = get_user_model()
from django.db import models, transaction


class City(models.Model):

    name = models.CharField(max_length=511)
    latitude = models.DecimalField(decimal_places=9, max_digits=11)
    longitude = models.DecimalField(decimal_places=9, max_digits=12)

    def __unicode__(self):
        return self.name


class CityKnowledge(models.Model):

    user = models.ForeignKey(User, related_name='known')
    city = models.ForeignKey(City, related_name='known_by')

    def __unicode__(self):
        return u"{0} {1} @ {2}".format(
            self.user.first_name,
            self.user.last_name,
            self.city
        )

    @transaction.atomic()
    def save(self, *args, **kwargs):
        CityKnowledge.objects.filter(
            city=self.city,
            user=self.user
        ).delete()
        super(CityKnowledge, self).save(*args, **kwargs)