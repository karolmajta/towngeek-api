# -*- coding: utf-8 -*-
from rest_framework.generics import ListCreateAPIView, \
    RetrieveDestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from filthy.views import WrappedResultMixin, FilterMixin

from towngeek.commons.permissions import IsObjectOwner

from towngeek.ratings.models import Bookmark
from towngeek.ratings.serializers.bookmarks import BookmarkSerializer


class BookmarkDetailView(WrappedResultMixin, RetrieveDestroyAPIView):

    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsObjectOwner('issued_by', allow_read=True),)


class BookmarkListCreateView(
        WrappedResultMixin,
        FilterMixin,
        ListCreateAPIView):

    queryset = Bookmark.objects.order_by('-issued_by').all()
    serializer_class = BookmarkSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    paginate_by = 10

    filters = {
        'user': ('issued_by', lambda val: int(val)),
        'question': ('question', lambda val: int(val)),
    }

    def pre_save(self, obj):
        obj.issued_by = self.request.user