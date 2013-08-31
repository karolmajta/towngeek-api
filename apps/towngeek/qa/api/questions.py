# -*- coding: utf-8 -*-
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from filthy.views import WrappedResultMixin

from towngeek.qa.models import Question


class QuestionDetailView(WrappedResultMixin, RetrieveAPIView):

    model = Question


class QuestionListCreateView(ListCreateAPIView):

    model = Question

    paginate_by = 10