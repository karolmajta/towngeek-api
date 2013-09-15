# -*- coding: utf-8 -*-
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import permissions

from filthy.views import WrappedResultMixin, FilterMixin

from towngeek.commons.permissions import IsObjectOwner
from towngeek.locations.models import CityKnowledge
from towngeek.locations.serializers.cityknowledges import \
    CityKnowledgeSerializer, WritableCityKnowledgeSerializer


class CityKnowledgeDetailView(WrappedResultMixin, RetrieveDestroyAPIView):

    queryset = CityKnowledge.objects.select_related('user', 'city')
    serializer_class = CityKnowledgeSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsObjectOwner('user', allow_read=True),)


class CityKnowledgeListCreateView(FilterMixin, ListCreateAPIView):

    queryset = CityKnowledge.objects.select_related('user', 'city')

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    paginate_by = 100

    filters = {
        'user': ('user__id', lambda val: int(val)),
    }

    def pre_save(self, obj):
        obj.user = self.request.user

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return CityKnowledgeSerializer
        else:
            return WritableCityKnowledgeSerializer

