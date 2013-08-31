# -*- coding: utf-8 -*-
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from filthy.views import WrappedResultMixin

from towngeek.qa.models import Question
from towngeek.qa.serializers.questions import QuestionSerializer


class QuestionDetailView(WrappedResultMixin, RetrieveAPIView):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionListCreateView(WrappedResultMixin, ListCreateAPIView):

    queryset = Question.objects.order_by('-issued_by').all()
    serializer_class = QuestionSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    paginate_by = 10

    def pre_save(self, obj):
        obj.issued_by = self.request.user