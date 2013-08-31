# -*- coding: utf-8 -*-
from rest_framework.generics import ListAPIView, RetrieveAPIView

from filthy.views import WrappedResultMixin

from towngeek.locations.models import City


class CityDetailView(WrappedResultMixin, RetrieveAPIView):

    model = City


class CityListView(ListAPIView):

    model = City

    paginate_by = 10
