# -*- coding: utf-8 -*-
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from filthy.views import WrappedResultMixin

from towngeek.commons.permissions import IsObjectOwner
from towngeek.locations.models import CityKnowledge
from towngeek.locations.serializers import CityKnowledgeSerializer


class CityKnowledgeDetailView(WrappedResultMixin, RetrieveDestroyAPIView):

    queryset = CityKnowledge.objects.all()
    serializer_class = CityKnowledgeSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsObjectOwner('user', allow_read=True),)


class CityKnowledgeListCreateView(ListCreateAPIView):

    queryset = CityKnowledge.objects.all()
    serializer_class = CityKnowledgeSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    paginate_by = 10

    def pre_save(self, obj):
        obj.user = self.request.user
