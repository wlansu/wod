# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0018_auto_20150424_2347'),
        ('wod_rules', '0011_auto_20150421_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='MortalMerit',
            fields=[
                ('merit_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wod_rules.Merit')),
                ('character', models.ForeignKey(to='characters.MortalCharacter')),
            ],
            options={
                'abstract': False,
            },
            bases=('wod_rules.merit', models.Model),
        ),
        migrations.CreateModel(
            name='MortalSpecialty',
            fields=[
                ('specialty_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wod_rules.Specialty')),
                ('character', models.ForeignKey(to='characters.MortalCharacter')),
            ],
            options={
                'abstract': False,
            },
            bases=('wod_rules.specialty', models.Model),
        ),
        migrations.CreateModel(
            name='MortalVice',
            fields=[
                ('vice_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wod_rules.Vice')),
                ('character', models.ForeignKey(to='characters.MortalCharacter')),
            ],
            options={
                'abstract': False,
            },
            bases=('wod_rules.vice', models.Model),
        ),
        migrations.CreateModel(
            name='MortalVirtue',
            fields=[
                ('virtue_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wod_rules.Virtue')),
                ('character', models.ForeignKey(to='characters.MortalCharacter')),
            ],
            options={
                'abstract': False,
            },
            bases=('wod_rules.virtue', models.Model),
        ),
    ]
