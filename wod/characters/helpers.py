"""Helper functions for characters."""


class CalculateStaticVariables(object):

    """Helper class to calculate various static variables related to characters.

    i.e. Defense, Maximum health, etc.
    """

    def __init__(self, character, *args, **kwargs):
        self.character = character

    def _calculate_health(self):
        """Calculates the health attribute of the character.

        Health = Stamina + Size
        """
        self.character.health = self.character.stamina + self.character.size

    def _calculate_willpower(self):
        """Calculates the willpower attribute of the character.

        Willpower = Resolve + Composure
        """
        self.character.willpower = self.character.resolve + self.character.composure

    def _calculate_defense(self):
        """Calculate the defense attribute of the character.

        Defense = lowest of Dexterity or Wits
        """
        lowest_value = min([self.character.dexterity, self.character.wits])
        self.character.defense = lowest_value

    def _calculate_initiative(self):
        """Calculates the initiative modifier of the character.

        Initiative = Dexterity + Composure
        """
        self.character.initiative = self.character.dexterity + self.character.composure

    def _calculate_speed(self):
        """Calculates the speed attribute of the character.

        Speed = Strength + Dexterity
        """
        self.character.speed = self.character.size + self.character.strength + self.character.dexterity

    def calculate_all(self):
        """Convenience method to calculate all attributes at once."""
        raise NotImplementedError("The subclass should implement this method.")

