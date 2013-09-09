# -*- coding: utf-8 -*-
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.authentication import TokenAuthentication

from filthy.views import WrappedResultMixin

from towngeek.locations.models import City
from towngeek.locations.serializers.cities import CitySerializer


class CityDetailView(WrappedResultMixin, RetrieveAPIView):

    queryset = City.objects.all()
    serializer_class = CitySerializer

    authentication_classes = (TokenAuthentication,)


class CityListView(ListAPIView):

    queryset = City.objects.all()
    serializer_class = CitySerializer

    authentication_classes = (TokenAuthentication,)

    paginate_by = 10
