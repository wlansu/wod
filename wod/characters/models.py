# -*- coding: utf-8 -*-
"""Models for the characters application."""
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from mage_rules.helpers import CalculateMageStaticVariables
from mage_rules.models import (
    Path,
    Order,
)
from rules_variables.static_variables import ten_dot_choices, dot_choices, character_choices
from mage_rules.static_variables import consilium_rank_choices
from wod_rules.helpers import CalculateMortalStaticVariables


class BaseCharacter(models.Model):

    """Abstract Character model upon which all other character models will be based."""

    class Meta:
        abstract = True

    name = models.CharField(_("name"), help_text=_("Your character's real name."), max_length=50, unique=True)
    player = models.ForeignKey("users.User")
    xp = models.IntegerField(_("Experience points"), blank=True, null=True)
    intelligence = models.IntegerField(_("Intelligence"), choices=dot_choices, default=1)
    wits = models.IntegerField(_("Wits"), choices=dot_choices, default=1)
    resolve = models.IntegerField(_("Resolve"), choices=dot_choices, default=1)
    strength = models.IntegerField(_("Strength"), choices=dot_choices, default=1)
    dexterity = models.IntegerField(_("Dexterity"), choices=dot_choices, default=1)
    stamina = models.IntegerField(_("Stamina"), choices=dot_choices, default=1)
    presence = models.IntegerField(_("Presence"), choices=dot_choices, default=1)
    manipulation = models.IntegerField(_("Manipulation"), choices=dot_choices, default=1)
    composure = models.IntegerField(_("Composure"), choices=dot_choices, default=1)
    description = models.TextField(_("Description"), blank=True, null=True,
                                   help_text=_("A description of your character."))
    age = models.IntegerField(_("Age"))
    virtue = models.ForeignKey("wod_rules.Virtue")
    vice = models.ForeignKey("wod_rules.Vice")
    type = models.CharField(_("Character type"), choices=character_choices, max_length=25,
                            default=character_choices[0][0])  # Default is 'mortal'.
    is_npc = models.BooleanField(default=False)
    campaign = models.ForeignKey('users.Campaign')

    # Calculated fields
    health = models.IntegerField(_("Maximum Health"), null=True, blank=True)
    willpower = models.IntegerField(_("Willpower"), null=True, blank=True)
    size = models.IntegerField(_("Size"), default=5)
    speed = models.IntegerField(_("Speed"), null=True, blank=True)
    initiative = models.IntegerField(_("Initiative modifier"), null=True, blank=True)
    defense = models.IntegerField(_("Defense"), null=True, blank=True)
    armor = models.IntegerField(_("Armor"), null=True, blank=True)

    # Skills

    # Mental
    academics = models.IntegerField(_("Academics"), default=0, choices=dot_choices, null=True, blank=True)
    computer = models.IntegerField(_("Computer"), default=0, choices=dot_choices, null=True, blank=True)
    crafts = models.IntegerField(_("Crafts"), default=0, choices=dot_choices, null=True, blank=True)
    investigation = models.IntegerField(_("Investigation"), default=0, choices=dot_choices, null=True, blank=True)
    medicine = models.IntegerField(_("Medicine"), default=0, choices=dot_choices, null=True, blank=True)
    occult = models.IntegerField(_("Occult"), default=0, choices=dot_choices, null=True, blank=True)
    politics = models.IntegerField(_("Politics"), default=0, choices=dot_choices, null=True, blank=True)
    science = models.IntegerField(_("Science"), default=0, choices=dot_choices, null=True, blank=True)

    # Physical
    athletics = models.IntegerField(_("Athletics"), default=0, choices=dot_choices, null=True, blank=True)
    brawl = models.IntegerField(_("Brawl"), default=0, choices=dot_choices, null=True, blank=True)
    drive = models.IntegerField(_("Drive"), default=0, choices=dot_choices, null=True, blank=True)
    firearms = models.IntegerField(_("Firearms"), default=0, choices=dot_choices, null=True, blank=True)
    larceny = models.IntegerField(_("Larceny"), default=0, choices=dot_choices, null=True, blank=True)
    stealth = models.IntegerField(_("Stealth"), default=0, choices=dot_choices, null=True, blank=True)
    survival = models.IntegerField(_("Survival"), default=0, choices=dot_choices, null=True, blank=True)
    weaponry = models.IntegerField(_("Weaponry"), default=0, choices=dot_choices, null=True, blank=True)

    # Social
    animal_ken = models.IntegerField(_("Animal_ken"), default=0, choices=dot_choices, null=True, blank=True)
    empathy = models.IntegerField(_("Empathy"), default=0, choices=dot_choices, null=True, blank=True)
    expression = models.IntegerField(_("Expression"), default=0, choices=dot_choices, null=True, blank=True)
    intimidation = models.IntegerField(_("Intimidation"), default=0, choices=dot_choices, null=True, blank=True)
    persuasion = models.IntegerField(_("Persuasion"), default=0, choices=dot_choices, null=True, blank=True)
    socialize = models.IntegerField(_("Socialize"), default=0, choices=dot_choices, null=True, blank=True)
    streetwise = models.IntegerField(_("Streetwise"), default=0, choices=dot_choices, null=True, blank=True)
    subterfuge = models.IntegerField(_("Subterfuge"), default=0, choices=dot_choices, null=True, blank=True)

    @property
    def update_link(self):
        """Subclasses should implement this method themselves."""
        raise NotImplementedError()

    def calculate_static_variables(self):
        """Subclasses should implement this method themselves."""
        raise NotImplementedError()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.calculate_static_variables()
        super(BaseCharacter, self).save(force_insert=force_insert, force_update=force_update, using=using,
                                        update_fields=update_fields)


class PlayerCharacterManager(models.Manager):

    """Don't show the MortalNPC's."""

    def get_queryset(self):
        qs = super(PlayerCharacterManager, self).get_queryset()
        return qs.filter(is_npc=False)


@python_2_unicode_compatible
class MortalCharacter(BaseCharacter):

    """A Mortal character model."""

    morality = models.IntegerField(_("Morality"), choices=ten_dot_choices, default=7)
    objects = PlayerCharacterManager()

    class Meta:
        verbose_name = "mortal"
        verbose_name_plural = "mortals"
        ordering = ('-name',)

    def __str__(self):
        return u'{0}'.format(self.name)

    def calculate_static_variables(self):
        """Calculate the various static variables which are based on attributes, merits, etc."""
        CalculateMortalStaticVariables(self).calculate_all()

    @property
    def update_link(self):
        """The update url for this character."""
        return reverse('characters:update_mortal', kwargs={'pk': self.pk})


class NPCManager(models.Manager):

    """Only show the NPC's."""

    def get_queryset(self):
        qs = super(NPCManager, self).get_queryset()
        return qs.filter(is_npc=True)


class MortalNPC(MortalCharacter):

    """A Mortal NPC character."""

    player_description = models.TextField(_("Description"), blank=True, null=True,
                                          help_text=_("Players can add their own description for this character."))
    gm_notes = models.TextField(_("Description"), blank=True, null=True,
                                help_text=_("Special notes visible only to the GM"))

    objects = NPCManager()

    class Meta:
        verbose_name_plural = "mortal npc's"

    def __init__(self, *args, **kwargs):
        super(MortalNPC, self).__init__(*args, **kwargs)
        self.is_npc = True


@python_2_unicode_compatible
class MageCharacter(BaseCharacter):

    """A Mage character model, holds all specific mage information."""

    shadow_name = models.CharField(_("Shadow name"), max_length=50, blank=True, null=True)
    path = models.ForeignKey(Path)
    order = models.ForeignKey(Order, blank=True, null=True)
    rank_in_order = models.CharField(_("Rank within order"), max_length=50, blank=True, null=True,
                                     help_text=_("Only needed if you have a specific rank within your order."))
    consilium_rank = models.CharField(_("Rank within the Consilium"), max_length=50, choices=consilium_rank_choices,
                                      blank=True, null=True)
    arcane_xp = models.IntegerField(_("Arcane experience points"), blank=True, null=True)
    gnosis = models.IntegerField(_("Gnosis"), choices=ten_dot_choices, default=1)
    wisdom = models.IntegerField(_("Wisdom"), choices=ten_dot_choices, default=7)

    # Arcana
    death = models.IntegerField(_("Death"), default=0, choices=dot_choices, null=True, blank=True)
    fate = models.IntegerField(_("Fate"), default=0, choices=dot_choices, null=True, blank=True)
    forces = models.IntegerField(_("Forces"), default=0, choices=dot_choices, null=True, blank=True)
    life = models.IntegerField(_("Life"), default=0, choices=dot_choices, null=True, blank=True)
    matter = models.IntegerField(_("Matter"), default=0, choices=dot_choices, null=True, blank=True)
    mind = models.IntegerField(_("Mind"), default=0, choices=dot_choices, null=True, blank=True)
    prime = models.IntegerField(_("Prime"), default=0, choices=dot_choices, null=True, blank=True)
    space = models.IntegerField(_("Space"), default=0, choices=dot_choices, null=True, blank=True)
    spirit = models.IntegerField(_("Spirit"), default=0, choices=dot_choices, null=True, blank=True)
    time = models.IntegerField(_("Time"), default=0, choices=dot_choices, null=True, blank=True)

    # Calculated Fields
    mana = models.IntegerField(_("Maximum Mana"), default=0, blank=True, null=True)

    objects = PlayerCharacterManager()

    class Meta:
        verbose_name = "mage"
        verbose_name_plural = "mages"
        ordering = ('-shadow_name', '-name')

    def __str__(self):
        if self.shadow_name:
            return u'{0}'.format(self.shadow_name)

        return u'{0}'.format(self.name)

    def calculate_static_variables(self):
        """Calculate the various static variables which are based on attributes, merits, etc."""
        CalculateMageStaticVariables(self).calculate_all()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.calculate_static_variables()
        super(MageCharacter, self).save(force_insert=force_insert, force_update=force_update, using=using,
                                        update_fields=update_fields)

    @property
    def update_link(self):
        """The update url for this character."""
        return reverse('characters:update_mage', kwargs={'pk': self.pk})


class MageNPC(MageCharacter):

    """A Mage NPC character."""

    player_description = models.TextField(_("Description"), blank=True, null=True,
                                          help_text=_("Players can add their own description for this character."))
    gm_notes = models.TextField(_("Description"), blank=True, null=True,
                                help_text=_("Special notes visible only to the GM"))

    objects = NPCManager()

    class Meta:
        verbose_name_plural = "mage npc's"

    def __init__(self, *args, **kwargs):
        super(MageNPC, self).__init__(*args, **kwargs)
        self.is_npc = True
