# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arcanum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25, verbose_name='name')),
            ],
            options={
                'verbose_name_plural': 'arcana',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CharacterArcanum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dots', models.IntegerField(verbose_name='dots', choices=[(b'1', 1), (b'2', 2), (b'3', 3), (b'4', 4), (b'5', 5)])),
                ('arcanum', models.ForeignKey(to='mage_rules.Arcanum')),
                ('character', models.ForeignKey(related_name='arcana', to='characters.MageCharacter')),
            ],
            options={
                'verbose_name_plural': 'arcana',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=25, verbose_name='name')),
                ('inferior', models.ForeignKey(related_name='inferior', to='mage_rules.Arcanum')),
                ('ruling', models.ManyToManyField(related_name='ruling', to='mage_rules.Arcanum')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
