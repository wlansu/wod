# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0010_auto_20150416_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='magecharacter',
            name='consilium_rank',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Rank within the Consilium', choices=[(b'hierarch', b'Hierarch'), (b'councillor', b'Councillor'), (b'herald', b'Herald'), (b'provost', b'Provost')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='type',
            field=models.CharField(default=b'mortal', max_length=25, verbose_name='Character type', choices=[(b'mortal', b'Mortal'), (b'mage', b'Mage')]),
            preserve_default=True,
        ),
    ]
