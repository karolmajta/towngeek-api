# -*- coding: utf-8 -*-
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from filthy.views import WrappedResultMixin

from towngeek.qa.models import Answer


class AnswerDetailView(WrappedResultMixin, RetrieveAPIView):

    model = Answer


class AnswerListCreateView(ListCreateAPIView):

    model = Answer

    paginate_by = 10