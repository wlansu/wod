# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0012_magenpc_is_npc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='magenpc',
            name='is_npc',
        ),
    ]
