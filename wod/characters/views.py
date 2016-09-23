# -*- coding: utf-8 -*-
"""Views for everything related to characters."""
from braces.views import LoginRequiredMixin
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import redirect
from django.views.generic import ListView, TemplateView, FormView
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, SortableListMixin

from characters import models
from characters.forms import CreateMageForm, CreateMortalForm
from characters.models import MageCharacter, MageNPC, MortalNPC, MortalCharacter
from mage_rules.forms import MageMeritInline, MageSpecialtyInline, RoteInline
from mage_rules.models import MageSpecialty, MageMerit, Rote
from rules_variables.static_variables import character_choices, skill_list
from mage_rules.static_variables import consilium_ranks
from users.models import Campaign
from wod_rules.forms import MortalMeritInline, MortalSpecialtyInline
from wod_rules.models import MortalSpecialty, MortalMerit


class CampaignRequiredMixin(LoginRequiredMixin):

    """View mixin which verifies that the user is signed up for a campaign."""

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            if not request.user.campaigns.all():
                messages.add_message(request, messages.ERROR, _('You are not yet signed up for a Campaign.'))
                return redirect('users:signup')

        return super(CampaignRequiredMixin, self).dispatch(
            request, *args, **kwargs)


class CampaignRequiredFormMixin(FormView):

    def get_form(self, form_class):
        """Overridden to limit the campaign choices to the ones the user is subscribed to."""
        form = super(CampaignRequiredFormMixin, self).get_form(form_class)
        form.fields['campaign'].queryset = Campaign.objects.filter(users=self.request.user)
        return form


class ListCharacters(CampaignRequiredMixin, ListView):

    """Lists all characters, based on the current user.

    If no characters are created yet it will show the create character view instead.
    """

    template_name = 'characters/list.html'

    def get_queryset(self):
        """No general queryset since we have to provide many different sub-classes, i.e. Mages, Mortals, etc."""
        return None

    def get_specific_queryset(self, model):
        """Only show the current users Character objects within the activated Campaign.

        If no Campaign is found None will be returned.
        """
        try:
            campaign = Campaign.objects.get(id=self.request.session['campaign'])
        except (Campaign.DoesNotExist, KeyError):
            return None
        qs = model.objects.filter(player=self.request.user)
        return qs.exclude(is_npc=True).filter(campaign=campaign)

    def mages(self):
        return self.get_specific_queryset(models.MageCharacter)

    def mortals(self):
        return self.get_specific_queryset(models.MortalCharacter)

    def dispatch(self, request, *args, **kwargs):
        """Redirect to create view if there are no characters for the current user."""
        if not any([self.mages(), self.mortals()]):
            return redirect('characters:create_choice')

        return super(ListCharacters, self).dispatch(request, *args, **kwargs)


class ListNPC(CampaignRequiredMixin, TemplateView):

    """View to select which NPC list to display."""

    template_name = 'characters/list_npcs.html'


class ListMortalNPC(CampaignRequiredMixin, ListView):

    """List all MortalNPC objects."""

    template_name = 'characters/mortal_npcs.html'
    context_object_name = 'npcs'
    model = MortalNPC

    def get_queryset(self):
        """Return only the currently activated campaign's MortalNPC objects or None."""
        try:
            campaign = Campaign.objects.get(id=self.request.session['campaign'])
            return MortalNPC.objects.filter(campaign=campaign)
        except Campaign.DoesNotExist:
            return None


class ListMageNPC(CampaignRequiredMixin, SortableListMixin, ListView):

    """List all MageNPC objects."""

    template_name = 'characters/mage_npcs.html'
    context_object_name = 'npcs'
    model = MageNPC
    sort_fields = ['order', 'path']

    def hierarch(self):
        """Add the Hierarch to the view or return None if there is no Hierarch."""
        try:
            return self.get_queryset().filter(consilium_rank=consilium_ranks[0].lower())[0]
        except IndexError:
            return None

    def councillors(self):
        return self.get_queryset().filter(consilium_rank=consilium_ranks[1].lower())

    def heralds(self):
        return self.get_queryset().filter(consilium_rank=consilium_ranks[2].lower())

    def provosts(self):
        return self.get_queryset().filter(consilium_rank=consilium_ranks[3].lower())

    def get_context_data(self, **kwargs):
        """Remove the consilium members, since they are shown separately."""
        data = super(ListMageNPC, self).get_context_data(**kwargs)
        data['npcs'] = data['npcs'].exclude(consilium_rank__isnull=False)
        return data

    def get_queryset(self):
        """Return only the currently activated campaign's MageNPC objects or None."""
        try:
            campaign = Campaign.objects.get(id=self.request.session['campaign'])
            qs = MageNPC.objects.filter(campaign=campaign)
            return self._sort_queryset(qs)
        except Campaign.DoesNotExist:
            return None


class CreateCharacterChoice(CampaignRequiredMixin, TemplateView):

    """View to select which type of character to create."""

    template_name = 'characters/create_choice.html'


class BaseCreateCharacterView(CampaignRequiredMixin, CampaignRequiredFormMixin, CreateWithInlinesView):

    """View on which all create character views are based.

    Provides:
        - Checks if the user is signed up for a campaign.
        - Limits campaign choices to only those the character is signed up for.
        - Inline formsets.
        - Sets the player and character on the necessary forms.
    """

    character_type = character_choices[0][0]  # default Mortal

    def forms_valid(self, form, inlines):
        """Sets the player attribute on the Character form and the character on the merit and specialty forms."""
        form.instance.player = self.request.user
        form.instance.type = self.character_type
        self.object = form.save()
        for formset in inlines:
            for form in formset:
                form.character = self.object
            formset.save()
        return redirect(self.success_url)


class BaseUpdateCharacterView(CampaignRequiredMixin, CampaignRequiredFormMixin, UpdateWithInlinesView):

    """View on which all update character views are based.

    Provides:
        - Checks if the user is signed up for a campaign.
        - Limits campaign choices to only those the character is signed up for.
        - Inline formsets.
        - Sets the character on the necessary forms.
        - Adds the specialties to the skills.
    """

    def forms_valid(self, form, inlines):
        """Sets the character on the merit and specialty forms."""
        self.object = form.save()
        for formset in inlines:
            for form in formset:
                form.character = self.object
            formset.save()
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        """Add the context to the view.

        Also sets all skills for which this character has a specialty as an attribute on the view, with the specialties
        as a list. This way they can be displayed nicely in the form.
        """
        context = super(BaseUpdateCharacterView, self).get_context_data(**kwargs)
        specialties = self.specialties()
        for specialty in specialties:
            if specialty.skill in skill_list:
                try:
                    x = getattr(BaseUpdateCharacterView, specialty.skill)
                    if specialty not in x:
                        x.append(specialty)
                except AttributeError:
                    setattr(BaseUpdateCharacterView, specialty.skill, [specialty])

        return context

    def specialties(self):
        """Add Specialties to the view."""
        raise NotImplementedError()

    def merits(self):
        """Add Merits to the view."""
        raise NotImplementedError()


class CreateMortalCharacter(BaseCreateCharacterView):

    """Create a MortalCharacter."""

    template_name = 'characters/base_create.html'

    form_class = CreateMortalForm
    model = MortalCharacter
    success_url = 'characters:list'
    inlines = [MortalMeritInline, MortalSpecialtyInline]


class UpdateMortalCharacter(BaseUpdateCharacterView):

    """Update a MortalCharacter."""

    template_name = 'characters/base_create.html'
    form_class = CreateMortalForm
    model = MortalCharacter
    success_url = 'characters:list'
    inlines = [MortalMeritInline, MortalSpecialtyInline]

    def specialties(self):
        """Add Specialties to the view."""
        return MortalSpecialty.objects.filter(character=self.get_object()).order_by('skill')

    def merits(self):
        """Add Merits to the view."""
        return MortalMerit.objects.filter(character=self.get_object())


class CreateMageCharacter(BaseCreateCharacterView):

    """Create a MageCharacter."""

    template_name = 'characters/create_mage.html'
    form_class = CreateMageForm
    model = MageCharacter
    success_url = 'characters:list'
    inlines = [MageMeritInline, MageSpecialtyInline, RoteInline]
    character_type = character_choices[1][0]  # Mage


class UpdateMageCharacter(BaseUpdateCharacterView):

    """Update a MageCharacter."""

    template_name = 'characters/create_mage.html'
    form_class = CreateMageForm
    model = MageCharacter
    success_url = 'characters:list'
    inlines = [MageMeritInline, MageSpecialtyInline, RoteInline]

    def specialties(self):
        """Add Specialties to the view."""
        return MageSpecialty.objects.filter(character=self.get_object()).order_by('skill')

    def merits(self):
        """Add Merits to the view."""
        return MageMerit.objects.filter(character=self.get_object())

    def rotes(self):
        """Add Rotes to the view."""
        return Rote.objects.filter(character=self.get_object())
