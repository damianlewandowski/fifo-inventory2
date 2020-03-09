from django.contrib import admin
from .models import Sold, Bought


@admin.register(Sold)
class SoldAdmin(admin.ModelAdmin):
    pass


@admin.register(Bought)
class BoughtAdmin(admin.ModelAdmin):
    pass
