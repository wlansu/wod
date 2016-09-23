"""Forms for the mage_rules app."""
from extra_views import InlineFormSet

from mage_rules.models import MageMerit, MageSpecialty, Rote


class InlineMixin(InlineFormSet):

    """Adds a prefix to the formset kwargs."""

    prefix = None

    def get_formset_kwargs(self):
        """Add the right prefix to the formset."""
        kwargs = super(InlineMixin, self).get_formset_kwargs()
        kwargs['prefix'] = self.prefix

        return kwargs


class MageMeritInline(InlineMixin):

    """
    Form to create multiple merits inline, meant to be used in conjunction with a Character Create form.
    """

    model = MageMerit
    fields = ('name', 'dots', 'cost', 'description')
    extra = 1
    can_delete = True
    prefix = 'Merits'


class MageSpecialtyInline(InlineMixin):

    """
    Form to create multiple specialties inline, meant to be used in conjunction with a Character Create form.
    """

    model = MageSpecialty
    fields = ('name', 'cost', 'skill', 'description')
    extra = 1
    can_delete = True
    prefix = 'Specialties'


class RoteInline(InlineMixin):

    """
    Form to create multiple rotes inline, meant to be used in conjunction with a Character Create form.
    """

    model = Rote
    fields = ('name', 'dice', 'description')
    extra = 1
    can_delete = True
    prefix = 'Rotes'
