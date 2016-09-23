# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wod_rules', '0007_auto_20150416_0934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialty',
            name='dots',
        ),
    ]
