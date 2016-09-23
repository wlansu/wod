# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0003_auto_20150410_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='magecharacter',
            name='mana',
            field=models.IntegerField(default=0, verbose_name='Maximum Mana'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='gnosis',
            field=models.IntegerField(default=0, verbose_name='Gnosis', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='health',
            field=models.IntegerField(default=0, verbose_name='Maximum Health'),
            preserve_default=True,
        ),
    ]
