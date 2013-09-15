from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

from towngeek.commons.handlers import track
from towngeek.locations.models import City


class Question(models.Model):

    issued_by = models.ForeignKey(User, related_name='questions')
    issued_at = models.DateTimeField(auto_now_add=True)
    city = models.ForeignKey(City, related_name='questions')
    text = models.TextField()
    bookmark_count = models.IntegerField(default=0)
    answer_count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.text[:100]


class Answer(models.Model):

    issued_by = models.ForeignKey(User, related_name='answers')
    issued_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, related_name='answers')
    text = models.TextField()
    score = models.IntegerField(default=0)

    def __unicode__(self):
        return self.text[:100]

track.count(Answer, 'question', 'answers', 'answer_count', dt=5)