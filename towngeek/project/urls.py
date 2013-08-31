from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import towngeek.locations.urls
import towngeek.qa.urls
import towngeek.ratings.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^locations/', include(towngeek.locations.urls)),
    url(r'^qa/', include(towngeek.qa.urls)),
    url(r'^ratings/', include(towngeek.ratings.urls)),

    url(r'^admin/', include(admin.site.urls)),
)
