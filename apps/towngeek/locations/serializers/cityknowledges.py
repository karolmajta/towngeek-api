# -*- coding: utf-8 -*-
from rest_framework import serializers

from towngeek.locations.models import CityKnowledge


class CityKnowledgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CityKnowledge
        fields = ('id', 'user', 'city')
        read_only_fields = ('id', 'user')