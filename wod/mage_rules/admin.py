# -*- coding: utf-8 -*-
"""Admin pages for the mage_rules app."""
__author__ = 'Wouter Lansu'
from django.contrib import admin

from mage_rules import models


@admin.register(models.Path, models.Order)
class MageAdmin(admin.ModelAdmin):
    pass

