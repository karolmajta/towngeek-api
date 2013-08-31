# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

import api.questions
import api.answers

urlpatterns = patterns('',
    url(r'^questions/$', api.questions.QuestionListCreateView.as_view()),
    url(r'^questions/(?P<pk>\d+)', api.questions.QuestionDetailView.as_view()),
    url(r'^answers/$', api.answers.AnswerListCreateView.as_view()),
    url(r'^answers/(?P<pk>\d+)', api.answers.AnswerDetailView.as_view()),
)
