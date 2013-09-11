# -*- coding: utf-8 -*-
from rest_framework import serializers

from towngeek.locations.models import CityKnowledge
from towngeek.locations.serializers.cities import CitySerializer
from towngeek.commons.serializers.users import SafeUserSerializer


class CityKnowledgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CityKnowledge
        fields = ('id', 'user', 'city')
        read_only_fields = ('id',)

    user = SafeUserSerializer()
    city = CitySerializer()


class WritableCityKnowledgeSerializer(CityKnowledgeSerializer):

    class Meta(CityKnowledgeSerializer.Meta):
        pass

    user = serializers.PrimaryKeyRelatedField(read_only=True)
    city = serializers.PrimaryKeyRelatedField()