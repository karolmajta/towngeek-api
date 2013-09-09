# -*- coding: utf-8 -*-
from rest_framework import serializers

from towngeek.qa.models import Answer
from towngeek.commons.serializers.users import SafeUserSerializer
from towngeek.ratings.models import Vote


class MyVoteField(serializers.Field):

    def to_native(self, obj):
        user = self.context['request'].user
        if user.is_anonymous():
            return 0
        else:
            try:
                return Vote.objects.get(issued_by=user, answer=obj).value
            except Vote.DoesNotExist:
                return 0


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = (
            'id',
            'issued_at',
            'issued_by',
            'question',
            'text',
            'score',
            'my_vote',
        )
        read_only_fields = ('id', 'issued_at', 'score')

    issued_by = SafeUserSerializer(read_only=True)
    my_vote = MyVoteField(source='*')