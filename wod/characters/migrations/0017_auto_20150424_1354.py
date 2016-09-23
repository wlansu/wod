# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0016_auto_20150424_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magecharacter',
            name='death',
            field=models.IntegerField(default=0, null=True, verbose_name='Death', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='fate',
            field=models.IntegerField(default=0, null=True, verbose_name='Fate', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='forces',
            field=models.IntegerField(default=0, null=True, verbose_name='Forces', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='life',
            field=models.IntegerField(default=0, null=True, verbose_name='Life', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='matter',
            field=models.IntegerField(default=0, null=True, verbose_name='Matter', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='mind',
            field=models.IntegerField(default=0, null=True, verbose_name='Mind', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='prime',
            field=models.IntegerField(default=0, null=True, verbose_name='Prime', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='space',
            field=models.IntegerField(default=0, null=True, verbose_name='Space', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='spirit',
            field=models.IntegerField(default=0, null=True, verbose_name='Spirit', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='time',
            field=models.IntegerField(default=0, null=True, verbose_name='Time', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
    ]
