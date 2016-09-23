"""Static variables specific to mage rules."""
from datetime import time


gnosis_variables = {
    0: {
        'attribute_max': 5,
        'max_mana': 0,
        'mana_per_turn': 0,
        'aura': 0,
        'base_paradox_pool': 1,
        'time_per_roll': time(hour=3)
    },
    1: {
        'attribute_max': 5,
        'max_mana': 10,
        'mana_per_turn': 1,
        'aura': 0,
        'base_paradox_pool': 1,
        'time_per_roll': time(hour=3)
    },
    2: {
        'attribute_max': 5,
        'max_mana': 11,
        'mana_per_turn': 2,
        'aura': 0,
        'base_paradox_pool': 1,
        'time_per_roll': time(hour=3)
    },
    3: {
        'attribute_max': 5,
        'max_mana': 12,
        'mana_per_turn': 3,
        'aura': 0,
        'base_paradox_pool': 2,
        'time_per_roll': time(hour=1)
    },
    4: {
        'attribute_max': 5,
        'max_mana': 13,
        'mana_per_turn': 4,
        'aura': 0,
        'base_paradox_pool': 2,
        'time_per_roll': time(hour=1)
    },
    5: {
        'attribute_max': 5,
        'max_mana': 14,
        'mana_per_turn': 5,
        'aura': 0,
        'base_paradox_pool': 3,
        'time_per_roll': time(minute=30)
    },
    6: {
        'attribute_max': 6,
        'max_mana': 15,
        'mana_per_turn': 6,
        'aura': 1,
        'base_paradox_pool': 3,
        'time_per_roll': time(minute=30)
    },
    7: {
        'attribute_max': 7,
        'max_mana': 20,
        'mana_per_turn': 7,
        'aura': 2,
        'base_paradox_pool': 4,
        'time_per_roll': time(minute=10)
    },
    8: {
        'attribute_max': 8,
        'max_mana': 30,
        'mana_per_turn': 8,
        'aura': 3,
        'base_paradox_pool': 4,
        'time_per_roll': time(minute=10)
    },
    9: {
        'attribute_max': 9,
        'max_mana': 50,
        'mana_per_turn': 10,
        'aura': 4,
        'base_paradox_pool': 5,
        'time_per_roll': time(minute=1)
    },
    10: {
        'attribute_max': 10,
        'max_mana': 100,
        'mana_per_turn': 15,
        'aura': 5,
        'base_paradox_pool': 5,
        'time_per_roll': time(minute=1)
    },
}

consilium_ranks = [
    'hierarch',
    'councillor',
    'herald',
    'provost',
]

consilium_rank_choices = tuple((x, x.title()) for x in consilium_ranks)

arcanas = [
    'death',
    'fate',
    'forces',
    'life',
    'matter',
    'mind',
    'prime',
    'space',
    'spirit',
    'time',
]

arcana_choices = tuple((x, x.title()) for x in arcanas)
