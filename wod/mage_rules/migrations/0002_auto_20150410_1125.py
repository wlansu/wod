# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0003_auto_20150410_1125'),
        ('wod_rules', '0002_auto_20150410_1125'),
        ('mage_rules', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MageMerit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dots', models.IntegerField(verbose_name='dots', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('character', models.ForeignKey(related_name='merits', to='characters.MageCharacter')),
                ('merit', models.ForeignKey(to='wod_rules.Merit')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MageSkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dots', models.IntegerField(verbose_name='dots', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('character', models.ForeignKey(related_name='skills', to='characters.MageCharacter')),
                ('skill', models.ForeignKey(to='wod_rules.Skill')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MageVice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('character', models.ForeignKey(to='characters.MageCharacter')),
                ('virtue', models.ForeignKey(to='wod_rules.Vice')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MageVirtue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('character', models.ForeignKey(to='characters.MageCharacter')),
                ('virtue', models.ForeignKey(to='wod_rules.Virtue')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='arcanum',
            name='cost',
            field=models.IntegerField(default=1, verbose_name='Cost to purchase'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arcanum',
            name='cost_inferior',
            field=models.IntegerField(default=8, verbose_name='Cost to purchase if inferior'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arcanum',
            name='cost_ruling',
            field=models.IntegerField(default=6, verbose_name='Cost to purchase if ruling'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arcanum',
            name='unavailable',
            field=models.BooleanField(default=False, verbose_name='unavailable'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='characterarcanum',
            name='dots',
            field=models.IntegerField(verbose_name='dots', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
    ]
