# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0006_auto_20150410_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magecharacter',
            name='vice',
            field=models.ForeignKey(to='wod_rules.Vice'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='virtue',
            field=models.ForeignKey(to='wod_rules.Virtue'),
            preserve_default=True,
        ),
    ]
