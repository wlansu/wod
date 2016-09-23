# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0007_auto_20150410_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magecharacter',
            name='mana',
            field=models.IntegerField(default=0, null=True, verbose_name='Maximum Mana', blank=True),
            preserve_default=True,
        ),
    ]
