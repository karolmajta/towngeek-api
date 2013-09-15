# -*- coding: utf-8 -*-
from rest_framework import serializers

from towngeek.qa.models import Question
from towngeek.commons.serializers.users import SafeUserSerializer
from towngeek.locations.serializers.cities import CitySerializer
from towngeek.ratings.models import Bookmark


class IsBookmarkedField(serializers.Field):

    def to_native(self, obj):
        user = self.context['request'].user
        if user.is_anonymous():
            return False
        else:
            return Bookmark.objects \
                .filter(issued_by=user, question=obj) \
                .exists()


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = (
            'id',
            'issued_at',
            'issued_by',
            'city',
            'text',
            'bookmark_count',
            'is_bookmarked',
            'answer_count',
        )
        read_only_fields = ('id', 'issued_at', 'bookmark_count', 'answer_count')

    issued_by = SafeUserSerializer(read_only=True)
    city = CitySerializer()
    is_bookmarked = IsBookmarkedField(source='*')


class WritableQuestionSerializer(QuestionSerializer):

    class Meta(QuestionSerializer.Meta):
        pass

    city = serializers.PrimaryKeyRelatedField()