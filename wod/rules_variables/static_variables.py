# -*- coding: utf-8 -*-
"""Static variables for the rules."""

dot_choices = tuple((x, str(x)) for x in range(0, 6))
ten_dot_choices = tuple((x, str(x)) for x in range(0, 11))

available_templates = [
    'mortal',
    'mage'
]

character_choices = tuple((x, x.title()) for x in available_templates)

skill_list = [
    'academics',
    'computer',
    'crafts',
    'investigation',
    'medicine',
    'occult',
    'politics',
    'science',
    'athletics',
    'brawl',
    'drive',
    'firearms',
    'larceny',
    'stealth',
    'survival',
    'weaponry',
    'animal_ken',
    'empathy',
    'expression',
    'intimidation',
    'persuasion',
    'socialize',
    'streetwise',
    'subterfuge'
]

skill_choices = tuple((x, x.title()) for x in skill_list)

attributes = [
    'intelligence',
    'wits',
    'resolve',
    'strength',
    'dexterity',
    'stamina',
    'presence',
    'manipulation',
    'composure',
]

attribute_choices = tuple((x, x.title()) for x in attributes)
