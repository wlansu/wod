# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterMerit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dots', models.IntegerField(verbose_name='dots', choices=[(b'1', 1), (b'2', 2), (b'3', 3), (b'4', 4), (b'5', 5)])),
                ('character', models.ForeignKey(related_name='merits', to='characters.MageCharacter')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CharacterSkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dots', models.IntegerField(verbose_name='dots', choices=[(b'1', 1), (b'2', 2), (b'3', 3), (b'4', 4), (b'5', 5)])),
                ('character', models.ForeignKey(related_name='skills', to='characters.MageCharacter')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Merit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25, verbose_name='name')),
                ('unavailable', models.BooleanField(default=False, verbose_name='unavailable')),
                ('min_dots', models.IntegerField(blank=True, null=True, verbose_name='minimum dots', choices=[(b'1', 1), (b'2', 2), (b'3', 3), (b'4', 4), (b'5', 5)])),
                ('max_dots', models.IntegerField(blank=True, null=True, verbose_name='maximum dots', choices=[(b'1', 1), (b'2', 2), (b'3', 3), (b'4', 4), (b'5', 5)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25, verbose_name='name')),
                ('unavailable', models.BooleanField(default=False, verbose_name='unavailable')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='merit',
            name='prerequisite_skills',
            field=models.ManyToManyField(to='wod_rules.Skill'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='characterskill',
            name='skill',
            field=models.ForeignKey(to='wod_rules.Skill'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='charactermerit',
            name='merit',
            field=models.ForeignKey(to='wod_rules.Merit'),
            preserve_default=True,
        ),
    ]
