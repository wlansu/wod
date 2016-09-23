# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0005_auto_20150410_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magecharacter',
            name='armor',
            field=models.IntegerField(null=True, verbose_name='Armor', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='defense',
            field=models.IntegerField(null=True, verbose_name='Defense', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='health',
            field=models.IntegerField(null=True, verbose_name='Maximum Health', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='initiative',
            field=models.IntegerField(null=True, verbose_name='Initiative modifier', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='speed',
            field=models.IntegerField(null=True, verbose_name='Speed', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='willpower',
            field=models.IntegerField(null=True, verbose_name='Willpower', blank=True),
            preserve_default=True,
        ),
    ]
