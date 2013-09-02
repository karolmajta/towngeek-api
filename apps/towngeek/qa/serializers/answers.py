# -*- coding: utf-8 -*-
from rest_framework import serializers

from towngeek.qa.models import Answer


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('id', 'issued_at', 'issued_by', 'question', 'text', 'score')
        read_only_fields = ('id', 'issued_at', 'issued_by', 'score')