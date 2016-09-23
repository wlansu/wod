# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0018_auto_20150424_2347'),
        ('mage_rules', '0008_magemerit_magespecialty_magevice_magevirtue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
                ('dice', models.IntegerField(null=True, verbose_name='dice', blank=True)),
                ('character', models.ForeignKey(to='characters.MageCharacter')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
