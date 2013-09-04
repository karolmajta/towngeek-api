# -*- coding: utf-8 -*-
import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException

import towngeek.commons.tasks


class MalformedStreamError(APIException):
    status_code = 400
    detail = "Could not read request stream."


class InvalidFormatError(APIException):
    status_code = 400
    detail = "Could not parse request as JSON."


class NotAListError(APIException):
    status_code = 400
    detaul = "Expecting JSON list."


class OnMandrillBounce(APIView):

    def head(self, request):
        return Response()

    def post(self, request):
#        try:
#            raw_body = request.stream.read()
#        except:
#            raise MalformedStreamError()
        try:
            l = json.loads(request.POST['mandrill_events'])
        except:
            raise InvalidFormatError()
        if not hasattr(l, '__iter__'):
            raise NotAListError(APIView)
        emails = []
        for elem in l:
            try:
                emails.append(elem['msg']['email'])
            except KeyError:
                pass  # we fail silently here to iterate over whole list

        data = {'emails': emails}

        towngeek.commons.tasks.deactivate_for_emails.delay(emails)
        return Response(data=data, status=status.HTTP_202_ACCEPTED)
