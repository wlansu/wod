# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0015_auto_20150421_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magecharacter',
            name='academics',
            field=models.IntegerField(default=0, null=True, verbose_name='Academics', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='animal_ken',
            field=models.IntegerField(default=0, null=True, verbose_name='Animal_ken', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='athletics',
            field=models.IntegerField(default=0, null=True, verbose_name='Athletics', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='brawl',
            field=models.IntegerField(default=0, null=True, verbose_name='Brawl', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='campaign',
            field=models.ForeignKey(related_name='character', default=1, to='users.Campaign'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='computer',
            field=models.IntegerField(default=0, null=True, verbose_name='Computer', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='crafts',
            field=models.IntegerField(default=0, null=True, verbose_name='Crafts', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='drive',
            field=models.IntegerField(default=0, null=True, verbose_name='Drive', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='empathy',
            field=models.IntegerField(default=0, null=True, verbose_name='Empathy', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='expression',
            field=models.IntegerField(default=0, null=True, verbose_name='Expression', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='firearms',
            field=models.IntegerField(default=0, null=True, verbose_name='Firearms', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='intimidation',
            field=models.IntegerField(default=0, null=True, verbose_name='Intimidation', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='investigation',
            field=models.IntegerField(default=0, null=True, verbose_name='Investigation', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='larceny',
            field=models.IntegerField(default=0, null=True, verbose_name='Larceny', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='medicine',
            field=models.IntegerField(default=0, null=True, verbose_name='Medicine', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='occult',
            field=models.IntegerField(default=0, null=True, verbose_name='Occult', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='persuasion',
            field=models.IntegerField(default=0, null=True, verbose_name='Persuasion', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='politics',
            field=models.IntegerField(default=0, null=True, verbose_name='Politics', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='science',
            field=models.IntegerField(default=0, null=True, verbose_name='Science', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='socialize',
            field=models.IntegerField(default=0, null=True, verbose_name='Socialize', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='stealth',
            field=models.IntegerField(default=0, null=True, verbose_name='Stealth', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='streetwise',
            field=models.IntegerField(default=0, null=True, verbose_name='Streetwise', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='subterfuge',
            field=models.IntegerField(default=0, null=True, verbose_name='Subterfuge', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='survival',
            field=models.IntegerField(default=0, null=True, verbose_name='Survival', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='weaponry',
            field=models.IntegerField(default=0, null=True, verbose_name='Weaponry', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
    ]
