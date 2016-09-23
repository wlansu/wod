# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wod_rules', '0004_auto_20150410_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cost', models.IntegerField(verbose_name='Cost to purchase')),
                ('name', models.CharField(max_length=25, verbose_name='name')),
                ('unavailable', models.BooleanField(default=False, verbose_name='unavailable')),
                ('min_dots', models.IntegerField(blank=True, null=True, verbose_name='minimum dots', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('max_dots', models.IntegerField(blank=True, null=True, verbose_name='maximum dots', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
