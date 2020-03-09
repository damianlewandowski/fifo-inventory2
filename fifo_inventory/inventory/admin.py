from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Sold, Bought


@admin.register(Sold)
class SoldAdmin(admin.ModelAdmin):
    pass


@admin.register(Bought)
class BoughtAdmin(admin.ModelAdmin):
    pass
