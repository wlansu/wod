# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mage_rules', '0006_auto_20150411_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='magemerit',
            name='character',
        ),
        migrations.RemoveField(
            model_name='magemerit',
            name='merit',
        ),
        migrations.DeleteModel(
            name='MageMerit',
        ),
        migrations.RemoveField(
            model_name='magespecialty',
            name='character',
        ),
        migrations.DeleteModel(
            name='MageSpecialty',
        ),
        migrations.RemoveField(
            model_name='magevice',
            name='character',
        ),
        migrations.RemoveField(
            model_name='magevice',
            name='virtue',
        ),
        migrations.DeleteModel(
            name='MageVice',
        ),
        migrations.RemoveField(
            model_name='magevirtue',
            name='character',
        ),
        migrations.RemoveField(
            model_name='magevirtue',
            name='virtue',
        ),
        migrations.DeleteModel(
            name='MageVirtue',
        ),
    ]
