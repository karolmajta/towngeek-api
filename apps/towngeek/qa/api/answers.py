# -*- coding: utf-8 -*-
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from filthy.views import WrappedResultMixin, FilterMixin

from towngeek.qa.models import Answer
from towngeek.qa.serializers.answers import AnswerSerializer


class AnswerDetailView(WrappedResultMixin, RetrieveAPIView):

    queryset = Answer.objects.select_related('issued_by').all()
    serializer_class = AnswerSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)


class AnswerListCreateView(WrappedResultMixin, FilterMixin, ListCreateAPIView):

    queryset = Answer.objects \
        .order_by('-score', '-issued_at') \
        .select_related('issued_by') \
        .all()
    serializer_class = AnswerSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    paginate_by = 10

    filters = {
        'question': ('question', lambda val: int(val)),
    }

    def pre_save(self, obj):
        obj.issued_by = self.request.user