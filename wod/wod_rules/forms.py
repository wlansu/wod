# -*- coding: utf-8 -*-
"""Forms for the wod_rules app."""
from extra_views import InlineFormSet
from wod_rules.models import MortalMerit, MortalSpecialty


class MortalMeritInline(InlineFormSet):

    """
    Form to create multiple merits inline, meant to be used in conjunction with a Character Create form.
    """

    model = MortalMerit
    fields = ('name', 'dots', 'cost', 'description')
    extra = 1
    can_delete = True


class MortalSpecialtyInline(InlineFormSet):

    """
    Form to create multiple specialties inline, meant to be used in conjunction with a Character Create form.
    """

    model = MortalSpecialty
    fields = ('name', 'cost', 'skill', 'description')
    extra = 1
    can_delete = True
