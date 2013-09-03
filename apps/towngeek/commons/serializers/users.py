# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework import serializers


class SafeUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')
        read_only_fields = ('id', 'username', 'first_name', 'last_name')


class UnsafeUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'token',
        )
        read_only_fields = ('id', 'username')

    token = serializers.CharField(read_only=True, source='auth_token.key')
    first_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)