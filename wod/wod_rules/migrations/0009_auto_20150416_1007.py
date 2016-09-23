# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wod_rules', '0008_remove_specialty_dots'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merit',
            name='cost',
            field=models.IntegerField(default=3, verbose_name='Cost to purchase'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='specialty',
            name='cost',
            field=models.IntegerField(default=3, verbose_name='Cost to purchase'),
            preserve_default=True,
        ),
    ]
