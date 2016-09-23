# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MageCharacter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text="Your character's real name.", unique=True, max_length=100, verbose_name='name')),
                ('shadow_name', models.CharField(max_length=100, null=True, verbose_name='Shadow name', blank=True)),
            ],
            options={
                'verbose_name_plural': 'mages',
            },
            bases=(models.Model,),
        ),
    ]
