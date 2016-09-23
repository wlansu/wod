# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mage_rules', '0002_auto_20150410_1125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mageskill',
            name='character',
        ),
        migrations.RemoveField(
            model_name='mageskill',
            name='skill',
        ),
        migrations.DeleteModel(
            name='MageSkill',
        ),
    ]
