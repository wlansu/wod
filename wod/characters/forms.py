# -*- coding: utf-8 -*-
"""Forms for the characters app."""
from django import forms

from characters.models import MageCharacter, MortalCharacter


class BaseCreateCharacterForm(forms.ModelForm):

    """Base form on which all character creation forms are based.

    Provides:
        - Adds an extra class to all fields for some nicer styling.
    """

    class Meta:
        model = MortalCharacter
        fields = []

    def __init__(self, *args, **kwargs):
        """Add an extra class to all fields for better styling."""
        super(BaseCreateCharacterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class CreateMortalForm(BaseCreateCharacterForm):

    """Create/Update a MortalCharacter."""

    class Meta:
        model = MortalCharacter
        fields = ['name', 'xp', 'morality',
                  'intelligence', 'strength', 'presence', 'wits', 'dexterity', 'manipulation', 'resolve',
                  'stamina', 'composure', 'description', 'health', 'willpower', 'size', 'initiative', 'defense',
                  'speed', 'armor', 'age', 'virtue', 'vice', 'academics', 'computer', 'crafts', 'investigation',
                  'medicine', 'occult', 'politics', 'science', 'athletics', 'brawl', 'drive', 'firearms', 'larceny',
                  'stealth', 'survival', 'weaponry', 'animal_ken', 'empathy', 'expression', 'intimidation', 'persuasion',
                  'socialize', 'streetwise', 'subterfuge', 'description', 'campaign']


class CreateMageForm(BaseCreateCharacterForm):

    """Create/Update a MageCharacter."""

    class Meta:
        model = MageCharacter
        fields = ['name', 'shadow_name', 'xp', 'arcane_xp', 'path', 'order', 'wisdom', 'gnosis', 'rank_in_order',
                  'intelligence', 'strength', 'presence', 'wits', 'dexterity', 'manipulation', 'resolve',
                  'stamina', 'composure', 'description', 'health', 'willpower', 'size', 'initiative', 'defense',
                  'speed', 'armor', 'age', 'virtue', 'vice', 'academics', 'computer', 'crafts', 'investigation',
                  'medicine', 'occult', 'politics', 'science', 'athletics', 'brawl', 'drive', 'firearms', 'larceny',
                  'stealth', 'survival', 'weaponry', 'animal_ken', 'empathy', 'expression', 'intimidation', 'persuasion',
                  'socialize', 'streetwise', 'subterfuge', 'death', 'matter', 'life', 'fate', 'spirit', 'prime',
                  'mind', 'space', 'time', 'forces', 'mana', 'description', 'campaign']
