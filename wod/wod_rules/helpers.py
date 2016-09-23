"""Helpers for the wod_rules app."""
from characters.helpers import CalculateStaticVariables


class CalculateMortalStaticVariables(CalculateStaticVariables):

    """Calculates all static variables for the character."""

    def calculate_all(self):
        self._calculate_health()
        self._calculate_willpower()
        self._calculate_defense()
        self._calculate_initiative()
        self._calculate_speed()
