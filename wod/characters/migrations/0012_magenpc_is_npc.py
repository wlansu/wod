# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0011_auto_20150418_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='magenpc',
            name='is_npc',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
