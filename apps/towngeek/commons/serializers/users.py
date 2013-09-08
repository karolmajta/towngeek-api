# -*- coding: utf-8 -*-
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework import serializers, fields


class SafeUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')
        read_only_fields = ('id', 'first_name', 'last_name')


class PasswordField(fields.WritableField):

    def from_native(self, value):
        return make_password(value)

    def to_native(self, value):
        return u""


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
            'password',
        )
        read_only_fields = ('id', 'username')

    token = serializers.CharField(read_only=True, source='auth_token.key')
    first_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = PasswordField()