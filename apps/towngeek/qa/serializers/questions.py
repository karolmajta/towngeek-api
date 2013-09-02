# -*- coding: utf-8 -*-
from rest_framework import serializers

from towngeek.qa.models import Question


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = (
            'id',
            'issued_at',
            'issued_by',
            'city', 'text',
            'bookmark_count'
        )
        read_only_fields = ('id', 'issued_at', 'issued_by', 'bookmark_count')