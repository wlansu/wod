# -*- coding: utf-8 -*-
"""All models having to do with the core WoD rules."""
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from rules_variables.static_variables import dot_choices, skill_choices


@python_2_unicode_compatible
class BaseMixin(models.Model):

    """Base class that contains shared fields."""

    class Meta:
        abstract = True

    cost = models.IntegerField(_("Cost to purchase"), default=3)
    name = models.CharField(_("name"), max_length=25)
    description = models.TextField(_("Description"), blank=True, null=True)

    def __str__(self):
        return u'{0}'.format(self.name)


class Merit(BaseMixin):

    """A merit that can be chosen by a character."""

    dots = models.IntegerField(_("Dots"), choices=dot_choices)


class Specialty(BaseMixin):

    """A Specialty that can be chosen by a Character."""

    skill = models.CharField(_("Skill"), choices=skill_choices, max_length=25)


@python_2_unicode_compatible
class Virtue(models.Model):

    """A Virtue that can be chosen by a character."""

    name = models.CharField(_("name"), max_length=25)

    def __str__(self):
        return u'{0}'.format(self.name)


@python_2_unicode_compatible
class Vice(models.Model):

    """A Vice that can be chosen by a character."""

    name = models.CharField(_("name"), max_length=25)

    def __str__(self):
        return u'{0}'.format(self.name)


class MortalMixin(models.Model):

    """Mixin that adds a MortalCharacter."""

    class Meta:
        abstract = True

    character = models.ForeignKey("characters.MortalCharacter")


class MortalMerit(Merit, MortalMixin):

    """A Merit tied to a MortalCharacter."""


class MortalSpecialty(Specialty, MortalMixin):

    """A Specialty tied to a MortalCharacter."""


class MortalVirtue(Virtue, MortalMixin):

    """A Virtue tied to a MortalCharacter."""


class MortalVice(Vice, MortalMixin):

    """A Vice tied to a MortalCharacter."""
