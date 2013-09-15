# -*- coding: utf-8 -*-
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import permissions

from filthy.views import WrappedResultMixin, FilterMixin

from towngeek.qa.models import Question
from towngeek.qa.serializers.questions import QuestionSerializer, \
    WritableQuestionSerializer


class QuestionDetailView(WrappedResultMixin, RetrieveAPIView):

    queryset = Question.objects.select_related('issued_by', 'city').all()
    serializer_class = QuestionSerializer


class QuestionListCreateView(FilterMixin, WrappedResultMixin, ListCreateAPIView):

    queryset = Question.objects \
        .order_by('-issued_at', '-bookmark_count') \
        .select_related('issued_by', 'city') \
        .all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    paginate_by = 10

    filters = {
        'city': ('city_id', lambda val: int(val)),
    }

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return QuestionSerializer
        else:
            return WritableQuestionSerializer

    def pre_save(self, obj):
        obj.issued_by = self.request.user
