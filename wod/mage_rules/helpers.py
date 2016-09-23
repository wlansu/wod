"""Helpers for Mage functionality."""
from characters.helpers import CalculateStaticVariables
from mage_rules.static_variables import gnosis_variables


class CalculateMageStaticVariables(CalculateStaticVariables):

    """Calculates all static variables for the character."""

    def _maximum_mana(self):
        """Set the maximum mana the mage can have."""
        self.character.mana = gnosis_variables[self.character.gnosis]['max_mana']

    def calculate_all(self):
        self._calculate_health()
        self._calculate_willpower()
        self._calculate_defense()
        self._calculate_initiative()
        self._calculate_speed()
        self._maximum_mana()
