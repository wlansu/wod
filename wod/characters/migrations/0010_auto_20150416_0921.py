# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0009_auto_20150414_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magecharacter',
            name='type',
            field=models.CharField(default=b'mortal', max_length=25, verbose_name='Character type', choices=[(b'mortal', b'mortal'), (b'mage', b'mage')]),
            preserve_default=True,
        ),
    ]
