from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.forms import ValidationError

from towngeek.qa.models import Question, Answer


class Bookmark(models.Model):

    issued_by = models.ForeignKey(User, related_name='bookmarks')
    question = models.ForeignKey(Question, related_name='bookmarks')
    issued_at = models.DateTimeField(auto_now_add=True)


class Vote(models.Model):

    VALUE_CHOICES = (
        (1, "UP"),
        (-1, "DOWN"),
    )

    issued_by = models.ForeignKey(User, related_name='votes')
    answer = models.ForeignKey(Answer, related_name='votes')
    issued_at = models.DateTimeField(auto_now_add=True)
    value = models.PositiveSmallIntegerField(choices=VALUE_CHOICES)

    def clean(self):
        if self.issued_by != self.answer.issued_by:
            raise ValidationError(
                "You are not allowed to vote on your own answers.",
                code='invalid',
            )