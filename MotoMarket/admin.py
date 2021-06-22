from django.contrib import admin

from MotoMarket.models import Sportbike, Quadro, Enduro, Cruiser, Country


admin.site.register(Sportbike)
admin.site.register(Cruiser)
admin.site.register(Quadro)
admin.site.register(Enduro)
admin.site.register(Country)