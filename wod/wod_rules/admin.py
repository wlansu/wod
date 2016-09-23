"""Admin classes for the wod_rules."""
from django.contrib import admin

from wod_rules import models


@admin.register(models.Virtue, models.Vice)
class WoDRulesAdmin(admin.ModelAdmin):
    pass
