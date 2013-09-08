from django.contrib import admin

import towngeek.locations.models

admin.site.register(towngeek.locations.models.City)
admin.site.register(towngeek.locations.models.CityKnowledge)
