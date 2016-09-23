# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0013_remove_magenpc_is_npc'),
    ]

    operations = [
        migrations.AddField(
            model_name='magecharacter',
            name='is_npc',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
