# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wod_rules', '0002_auto_20150410_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeritPrerequisiteSkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dots', models.IntegerField(blank=True, null=True, verbose_name='Dots', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('merit', models.ForeignKey(related_name='prerequisites', to='wod_rules.Merit')),
                ('skill', models.ForeignKey(to='wod_rules.Skill')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='merit',
            name='prerequisite_skills',
        ),
        migrations.AddField(
            model_name='merit',
            name='increase_amount',
            field=models.IntegerField(null=True, verbose_name='Increase amount', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='merit',
            name='increases',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Increases', choices=[(b'size', b'size')]),
            preserve_default=True,
        ),
    ]
