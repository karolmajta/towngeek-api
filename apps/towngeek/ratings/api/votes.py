# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from filthy.views import WrappedResultMixin

from towngeek.commons.permissions import IsObjectOwner

from towngeek.ratings.models import Vote


class VoteDetailView(WrappedResultMixin, RetrieveUpdateDestroyAPIView):

    model = Vote
    queryset = Vote.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsObjectOwner('issued_by', allow_read=True),)


class VoteListCreateView(WrappedResultMixin, ListCreateAPIView):

    model = Vote
    queryset = Vote.objects.order_by('-issued_by').all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    paginate_by = 10

    def pre_save(self, obj):
        obj.issued_by = self.request.user