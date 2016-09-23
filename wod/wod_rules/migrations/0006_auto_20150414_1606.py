# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('wod_rules', '0005_specialty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meritprerequisiteskill',
            name='merit',
        ),
        migrations.DeleteModel(
            name='MeritPrerequisiteSkill',
        ),
        migrations.RemoveField(
            model_name='merit',
            name='increase_amount',
        ),
        migrations.RemoveField(
            model_name='merit',
            name='increases',
        ),
        migrations.RemoveField(
            model_name='merit',
            name='max_dots',
        ),
        migrations.RemoveField(
            model_name='merit',
            name='min_dots',
        ),
        migrations.RemoveField(
            model_name='merit',
            name='unavailable',
        ),
        migrations.RemoveField(
            model_name='specialty',
            name='max_dots',
        ),
        migrations.RemoveField(
            model_name='specialty',
            name='min_dots',
        ),
        migrations.RemoveField(
            model_name='specialty',
            name='unavailable',
        ),
        migrations.AddField(
            model_name='merit',
            name='content_type',
            field=models.ForeignKey(default=1, to='contenttypes.ContentType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='merit',
            name='description',
            field=models.TextField(null=True, verbose_name='Description', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='merit',
            name='dots',
            field=models.IntegerField(default=1, verbose_name='Dots', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='merit',
            name='object_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialty',
            name='content_type',
            field=models.ForeignKey(default=1, to='contenttypes.ContentType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialty',
            name='description',
            field=models.TextField(null=True, verbose_name='Description', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='specialty',
            name='dots',
            field=models.IntegerField(default=1, verbose_name='Dots', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialty',
            name='object_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialty',
            name='skill',
            field=models.CharField(default=1, max_length=25, verbose_name='Skill', choices=[(b'academics', b'academics'), (b'computer', b'computer'), (b'crafts', b'crafts'), (b'investigation', b'investigation'), (b'medicine', b'medicine'), (b'occult', b'occult'), (b'politics', b'politics'), (b'science', b'science'), (b'athletics', b'athletics'), (b'brawl', b'brawl'), (b'drive', b'drive'), (b'firearms', b'firearms'), (b'larceny', b'larceny'), (b'stealth', b'stealth'), (b'survival', b'survival'), (b'weaponry', b'weaponry'), (b'animal_ken', b'animal_ken'), (b'empathy', b'empathy'), (b'expression', b'expression'), (b'intimidation', b'intimidation'), (b'persuasion', b'persuasion'), (b'socialize', b'socialize'), (b'streetwise', b'streetwise'), (b'subterfuge', b'subterfuge')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='merit',
            name='cost',
            field=models.IntegerField(null=True, verbose_name='Cost to purchase', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='specialty',
            name='cost',
            field=models.IntegerField(null=True, verbose_name='Cost to purchase', blank=True),
            preserve_default=True,
        ),
    ]
