# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0010_auto_20150416_0921'),
        ('wod_rules', '0007_auto_20150416_0934'),
        ('mage_rules', '0007_auto_20150414_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='MageMerit',
            fields=[
                ('merit_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wod_rules.Merit')),
                ('character', models.ForeignKey(to='characters.MageCharacter')),
            ],
            options={
                'abstract': False,
            },
            bases=('wod_rules.merit', models.Model),
        ),
        migrations.CreateModel(
            name='MageSpecialty',
            fields=[
                ('specialty_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wod_rules.Specialty')),
                ('character', models.ForeignKey(to='characters.MageCharacter')),
            ],
            options={
                'abstract': False,
            },
            bases=('wod_rules.specialty', models.Model),
        ),
        migrations.CreateModel(
            name='MageVice',
            fields=[
                ('vice_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wod_rules.Vice')),
                ('character', models.ForeignKey(to='characters.MageCharacter')),
            ],
            options={
                'abstract': False,
            },
            bases=('wod_rules.vice', models.Model),
        ),
        migrations.CreateModel(
            name='MageVirtue',
            fields=[
                ('virtue_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wod_rules.Virtue')),
                ('character', models.ForeignKey(to='characters.MageCharacter')),
            ],
            options={
                'abstract': False,
            },
            bases=('wod_rules.virtue', models.Model),
        ),
    ]
