# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mage_rules', '0003_auto_20150410_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='characterarcanum',
            name='arcanum',
        ),
        migrations.RemoveField(
            model_name='characterarcanum',
            name='character',
        ),
        migrations.DeleteModel(
            name='CharacterArcanum',
        ),
        migrations.RemoveField(
            model_name='path',
            name='inferior',
        ),
        migrations.RemoveField(
            model_name='path',
            name='ruling',
        ),
        migrations.DeleteModel(
            name='Arcanum',
        ),
    ]
