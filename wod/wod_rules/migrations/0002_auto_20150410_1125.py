# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wod_rules', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25, verbose_name='name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Virtue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25, verbose_name='name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='charactermerit',
            name='character',
        ),
        migrations.RemoveField(
            model_name='charactermerit',
            name='merit',
        ),
        migrations.DeleteModel(
            name='CharacterMerit',
        ),
        migrations.RemoveField(
            model_name='characterskill',
            name='character',
        ),
        migrations.RemoveField(
            model_name='characterskill',
            name='skill',
        ),
        migrations.DeleteModel(
            name='CharacterSkill',
        ),
        migrations.AddField(
            model_name='merit',
            name='cost',
            field=models.IntegerField(default=3, verbose_name='Cost to purchase'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skill',
            name='cost',
            field=models.IntegerField(default=5, verbose_name='Cost to purchase'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skill',
            name='max_dots',
            field=models.IntegerField(blank=True, null=True, verbose_name='maximum dots', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='skill',
            name='mental',
            field=models.BooleanField(default=False, verbose_name='Mental'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='skill',
            name='min_dots',
            field=models.IntegerField(blank=True, null=True, verbose_name='minimum dots', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='skill',
            name='physical',
            field=models.BooleanField(default=False, verbose_name='Physical'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='skill',
            name='social',
            field=models.BooleanField(default=False, verbose_name='Social'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='merit',
            name='max_dots',
            field=models.IntegerField(blank=True, null=True, verbose_name='maximum dots', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='merit',
            name='min_dots',
            field=models.IntegerField(blank=True, null=True, verbose_name='minimum dots', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='merit',
            name='prerequisite_skills',
            field=models.ManyToManyField(to='wod_rules.Skill', null=True, blank=True),
            preserve_default=True,
        ),
    ]
