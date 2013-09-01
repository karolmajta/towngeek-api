# -*- coding: utf-8 -*-
from rest_framework import serializers

from towngeek.ratings.models import Vote


class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = ('id', 'issued_at', 'issued_by', 'answer', 'value')
        read_only_fields = ('id', 'issued_at', 'issued_by')