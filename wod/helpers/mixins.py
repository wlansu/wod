"""Mixins for the WoD package."""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from helpers.exceptions import InsufficientXPException, MinimumDotException, MaximumDotException


class PurchaseAllowedMixin(models.Model):
    # TODO: Move this functionality to the forms
    """Mixin that checks whether the purchase is allowed.

    If the purchase is allowed the cost is subtracted from the characters xp pool.

    Note: this mixin expects at least the following attributes:
        - self.dots
        - self.character

    Use this mixin for any class that can be purchased by a character.
    """

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        """Overridden in order to store the previous `dots` value.

        This is used to calculate the xp cost of increasing dots after an initial purchase.
        """
        super(PurchaseAllowedMixin, self).__init__(*args, **kwargs)
        self.old_dots = self.dots
        self.price = 0

    def check_xp(self, purchasing, arcana=False):
        """Check's whether or not the character has enough xp.

        If the character has enough xp, the xp is deducted.
        :param purchasing: The object the character is purchasing (i.e. a merit or a skill).
        :raises: `InsufficientXPException` if the character does not have enough xp.
        """
        if self.dots != self.old_dots:
            new_dots = list(range(1, self.dots))
            # Note: this only works for adding dots, subtracting is not supported.
            cost_dots = new_dots[self.old_dots:]
            for dot in cost_dots:
                cost = purchasing.cost
                if arcana:
                    cost = self.arcana_cost()
                self.price += dot * cost

            if self.character.xp < self.price:
                raise InsufficientXPException(
                    _("Your character has {0} experience points, but the cost is {1}").format(
                        self.character.xp, self.price))

    def pre_save(self):
        """Check whether the purchase is allowed."""
        if self.min_dots and self.dots < self.min_dots:
            raise MinimumDotException(_("You are required to purchase at least {0} dots.").format(self.min_dots))
        if self.max_dots and self.dots > self.max_dots:
            raise MaximumDotException(_("You cannot purchase more than {0} dots.").format(self.max_dots))

    def post_save(self):
        """Everything went well; subtract the dot cost from the character's xp."""
        self.character.xp -= self.price
        self.character.save(update_fields=['xp'])


class ArcanaPurchaseAllowedMixin(PurchaseAllowedMixin):

    """Special mixin for verifying the purchase of Arcana.

    Arcana are special in that they have differing cost based on whether the arcana is ruling, inferior or normal.
    """

    class Meta:
        abstract = True

    def check_xp(self, purchasing, arcana=True):
        """Overridden in order to set arcana to True."""
        return super(ArcanaPurchaseAllowedMixin, self).check_xp(purchasing, arcana=True)

    def arcana_cost(self):
        """Figure out what the cost for the Arcana is."""
        if self.purchasing in self.character.path.ruling:
            cost = self.purchasing.cost_ruling
        elif self.purchasing == self.character.path.inferior:
            cost = self.purchasing.cost_inferior
        else:
            cost = self.purchasing.cost_inferior

        return cost
