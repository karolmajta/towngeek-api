# -*- coding: utf-8 -*-
from rest_framework import serializers

from towngeek.ratings.models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bookmark
        fields = ('id', 'issued_at', 'issued_by', 'question')
        read_only_fields = ('id', 'issued_at', 'issued_by')