# -*- coding: utf-8 -*-
""""""
__author__ = 'Wouter Lansu'
from django.conf.urls import patterns, url

from characters import views

urlpatterns = patterns('',
    url(
        regex=r'^list/$',
        view=views.ListCharacters.as_view(),
        name='list'
    ),
    url(
        regex=r'^non-player-characters/$',
        view=views.ListNPC.as_view(),
        name='list_npcs'
    ),
    url(
        regex=r'^create/$',
        view=views.CreateCharacterChoice.as_view(),
        name='create_choice'
    ),
    url(
        regex=r'^mortal/create/$',
        view=views.CreateMortalCharacter.as_view(),
        name='create_mortal'
    ),
    url(
        regex=r'^mortal/(?P<pk>[\d+]+)/update',
        view=views.UpdateMortalCharacter.as_view(),
        name='update_mortal'
    ),
    url(
        regex=r'^mortal/non-player-characters/$',
        view=views.ListMortalNPC.as_view(),
        name='list_mortal_npcs'
    ),
    url(
        regex=r'^mage/create/$',
        view=views.CreateMageCharacter.as_view(),
        name='create_mage'
    ),
    url(
        regex=r'^mage/(?P<pk>[\d+]+)/update',
        view=views.UpdateMageCharacter.as_view(),
        name='update_mage'
    ),
    url(
        regex=r'^mage/non-player-characters/$',
        view=views.ListMageNPC.as_view(),
        name='list_mage_npcs'
    ),
)

