# -*- coding: utf-8 -*-
"""Admin pages for the characters app."""
__author__ = 'Wouter Lansu'
from django.contrib import admin

from characters import models


@admin.register(models.MortalCharacter, models.MortalNPC, models.MageCharacter, models.MageNPC)
class CharacterAdmin(admin.ModelAdmin):
    pass
