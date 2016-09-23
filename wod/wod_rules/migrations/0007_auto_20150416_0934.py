# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wod_rules', '0006_auto_20150414_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merit',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='merit',
            name='object_id',
        ),
        migrations.RemoveField(
            model_name='specialty',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='specialty',
            name='object_id',
        ),
    ]
