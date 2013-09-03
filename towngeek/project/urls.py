from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from rest_framework.views import APIView
from rest_framework.response import Response

import towngeek.commons.urls
import towngeek.commons.webhook_urls
import towngeek.locations.urls
import towngeek.qa.urls
import towngeek.ratings.urls


class APIRoot(APIView):

    def get(self, request):
        desc = [
            {'url': "/commons/users/", 'resource': "User list"},
            {'url': "/commons/users/:id", 'resource': "User details"},
            {'url': "/commons/token", 'resource': "Token (authentication)"},
            {'url': "/locations/cities/", 'resource': "City list"},
            {'url': "/locations/cities/:id", 'resource': "City details"},
            {'url': "/qa/questions/", 'resource': "Question list"},
            {'url': "/qa/questions/:id", 'resource': "Question details"},
            {'url': "/qa/answers/", 'resource': "Answer list"},
            {'url': "/qa/answers/:id", 'resource': "Answer details"},
            {'url': "/ratings/bookmarks/", 'resource': "Bookmark list"},
            {'url': "/ratings/bookmarks/:id", 'resource': "Bookmark details"},
            {'url': "/ratings/votes/", 'resource': "Vote list"},
            {'url': "/ratings/votes/:id", 'resource': "Vote details"},
        ]
        return Response(data={'results': desc})


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', APIRoot.as_view()),

    url(r'^commons/', include(towngeek.commons.urls)),
    url(r'^locations/', include(towngeek.locations.urls)),
    url(r'^qa/', include(towngeek.qa.urls)),
    url(r'^ratings/', include(towngeek.ratings.urls)),

    url(r'^webhooks/', include(towngeek.commons.webhook_urls)),

    url(r'^admin/', include(admin.site.urls)),
)