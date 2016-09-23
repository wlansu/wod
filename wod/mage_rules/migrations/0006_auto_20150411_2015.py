# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mage_rules', '0005_magespecialty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='magespecialty',
            name='specialty',
        ),
        migrations.AddField(
            model_name='magespecialty',
            name='description',
            field=models.CharField(max_length=255, null=True, verbose_name='Description', blank=True),
            preserve_default=True,
        ),
    ]
