# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework.exceptions import APIException
from rest_framework.views import APIView
from rest_framework.response import Response

from towngeek.commons.serializers.tokens import TokenSerializer
from towngeek.commons.serializers.credentials import CredentialsSerializer


class InvalidQueryParams(APIException):
    status_code = 400
    detail = _("Invalid GET params. Pleas provide `email` and `password`.")


class InvalidCredentials(APIException):
    status_code = 401
    detail = _("No token found for given credentials.")


class TokenDetailView(APIView):

    def get(self, request):
        credential_serializer = CredentialsSerializer(data=request.GET)
        if not credential_serializer.is_valid():
            raise InvalidQueryParams()
        safe_qp = credential_serializer.object
        try:
            user = User.objects.get(email=safe_qp['email'])
        except User.DoesNotExist:
            raise InvalidCredentials()
        if not user.check_password(safe_qp['password']):
            raise InvalidCredentials()
        data = {'result': TokenSerializer(user.auth_token).data}
        return Response(data=data)

