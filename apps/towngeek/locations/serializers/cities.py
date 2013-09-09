# -*- coding: utf-8 -*-
from rest_framework import serializers

from towngeek.locations.models import City, CityKnowledge


class IsKnownField(serializers.Field):

    def to_native(self, obj):
        user = self.context['request'].user
        if user.is_anonymous():
            return False
        else:
            return CityKnowledge.objects \
                .filter(user=user, city=obj) \
                .exists()


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('id', 'name', 'latitude', 'longitude', 'is_known')
        read_only_fields = ('id', 'name', 'latitude', 'longitude')

    is_known = IsKnownField(source='*')