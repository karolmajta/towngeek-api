# -*- coding: utf-8 -*-
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from filthy.views import WrappedResultMixin

from towngeek.qa.models import Answer
from towngeek.qa.serializers.answers import AnswerSerializer


class AnswerDetailView(WrappedResultMixin, RetrieveAPIView):

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerListCreateView(WrappedResultMixin, ListCreateAPIView):

    queryset = Answer.objects.order_by('-issued_at', '-score').all()
    serializer_class = AnswerSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    paginate_by = 10

    def pre_save(self, obj):
        obj.issued_by = self.request.user