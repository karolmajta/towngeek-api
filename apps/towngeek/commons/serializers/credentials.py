# -*- coding: utf-8 -*-

from rest_framework import serializers


class CredentialsSerializer(serializers.Serializer):

    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)