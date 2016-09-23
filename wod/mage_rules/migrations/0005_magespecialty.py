# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wod_rules', '0005_specialty'),
        ('characters', '0007_auto_20150410_1643'),
        ('mage_rules', '0004_auto_20150410_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='MageSpecialty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('character', models.ForeignKey(to='characters.MageCharacter')),
                ('specialty', models.ForeignKey(to='wod_rules.Specialty')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
