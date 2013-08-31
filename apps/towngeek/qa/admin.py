from django.contrib import admin

from towngeek.qa.models import Question, Answer


admin.site.register(Question)
admin.site.register(Answer)