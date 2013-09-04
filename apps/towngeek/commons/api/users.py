# -*- coding: utf-8 -*-
import uuid

from django.db import transaction, IntegrityError
from django.utils.translation import ugettext as _
from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
from rest_framework.exceptions import APIException
from rest_framework.authtoken.models import Token

from filthy.views import WrappedResultMixin

from towngeek.commons.serializers.users import SafeUserSerializer, \
    UnsafeUserSerializer


class UserDetailView(WrappedResultMixin, RetrieveAPIView):

    queryset = User.objects.all()
    serializer_class = SafeUserSerializer


class NonUniqueEmail(APIException):
    detail = _("User with given emiail already exists")
    status_code = 400


class UserListCreateView(WrappedResultMixin, ListCreateAPIView):

    authentication_classes = (TokenAuthentication,)

    paginate_by = 10

    username_generator = uuid

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return SafeUserSerializer
        else:
            return UnsafeUserSerializer

    def get_queryset(self):
        if self.request.method in permissions.SAFE_METHODS:
            return User.objects.all()
        else:
            return User.objects.select_relatet('token').all()

    def pre_save(self, obj):
        generator = self.__class__.username_generator
        obj.username = generator.uuid4()

    def create(self, *args, **kwargs):
        try:
            with transaction.atomic():
                result = super(
                    UserListCreateView,
                    self
                ).create(*args, **kwargs)
        except IntegrityError:
            raise NonUniqueEmail()
        return result

    def post_save(self, obj, created=False):
        print "post_save"
        print created
        if created:
            print "saving"
            Token.objects.create(user=obj)
            print "saved"