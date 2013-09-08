from django.db import models, transaction
from django.contrib.auth import get_user_model
User = get_user_model()

from towngeek.commons import aggregations
from towngeek.commons.handlers import track
from towngeek.qa.models import Question, Answer


class Bookmark(models.Model):

    class Meta:

        unique_together = (
            ('issued_by', 'question')
        )

    issued_by = models.ForeignKey(User, related_name='bookmarks')
    question = models.ForeignKey(Question, related_name='bookmarks')
    issued_at = models.DateTimeField(auto_now_add=True)

    @transaction.atomic()
    def save(self, *args, **kwargs):
        Bookmark.objects.filter(
            issued_by=self.issued_by,
            question=self.question
        ).delete()
        super(Bookmark, self).save(*args, **kwargs)

track.count(Bookmark, 'question', 'bookmarks', 'bookmark_count', dt=5)


class Vote(models.Model):

    class Meta:

        unique_together = (
            ('issued_by', 'answer')
        )

    VALUE_CHOICES = (
        (1, "UP"),
        (0, "NONE"),
        (-1, "DOWN"),
    )

    issued_by = models.ForeignKey(User, related_name='votes')
    answer = models.ForeignKey(Answer, related_name='votes')
    issued_at = models.DateTimeField(auto_now_add=True)
    value = models.PositiveSmallIntegerField(choices=VALUE_CHOICES)

    @transaction.atomic()
    def save(self, *args, **kwargs):
        Vote.objects.filter(
            issued_by=self.issued_by,
            answer=self.answer
        ).delete()
        super(Vote, self).save(*args, **kwargs)

track.aggregation(
    Vote, 'answer', 'votes', 'value', 'score', aggregations.Sum, empty=0, dt=5)