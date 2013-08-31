from django.contrib import admin

from towngeek.ratings.models import Bookmark, Vote

admin.site.register(Bookmark)
admin.site.register(Vote)