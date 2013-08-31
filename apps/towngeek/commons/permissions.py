# -*- coding: utf-8 -*-
from functools import partial

from rest_framework import permissions
from rest_framework.permissions import BasePermission


def _get_and_maybe_call(source, property_name):
    prop = getattr(source, property_name)
    if hasattr(prop, '__call__'):
        return prop()
    else:
        return prop


def IsObjectOwner(owner_field, allow_read=False, base=BasePermission):

    class Perm(base):

        def has_object_permission(self, request, view, obj):
            if request.method in permissions.SAFE_METHODS and allow_read:
                return True
            else:
                owner = _get_and_maybe_call(obj, owner_field)
                return owner == request.user

    return Perm

