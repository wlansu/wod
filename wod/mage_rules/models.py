# -*- coding: utf-8 -*-
"""All models for rules pertaining specifically to mages."""
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from wod_rules.models import Merit, Specialty, Virtue, Vice


@python_2_unicode_compatible
class Path(models.Model):

    """A Path."""

    name = models.CharField(_("name"), max_length=25, unique=True)

    def __str__(self):
        return u'{0}'.format(self.name)


@python_2_unicode_compatible
class Order(models.Model):

    """An Order."""

    name = models.CharField(_("name"), max_length=100, unique=True)

    def __str__(self):
        return u'{0}'.format(self.name)


class MageMixin(models.Model):

    """Mixin that adds a MageCharacter."""

    class Meta:
        abstract = True

    character = models.ForeignKey("characters.MageCharacter")


class MageMerit(Merit, MageMixin):

    """A Merit tied to a MageCharacter."""


class MageSpecialty(Specialty, MageMixin):

    """A Specialty tied to a MageCharacter."""


class MageVirtue(Virtue, MageMixin):

    """A Virtue tied to a MageCharacter."""


class MageVice(Vice, MageMixin):

    """A Vice tied to a MageCharacter."""


class Rote(models.Model):

    """A Rote tied to a MageCharacter."""

    name = models.CharField(_("name"), max_length=100, unique=True)
    description = models.TextField(_("description"))
    dice = models.IntegerField(_("dice"), null=True, blank=True)
    character = models.ForeignKey("characters.MageCharacter")
