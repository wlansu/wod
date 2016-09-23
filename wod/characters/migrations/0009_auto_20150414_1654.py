# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0008_auto_20150411_2015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='magecharacter',
            options={'verbose_name': 'mage', 'verbose_name_plural': 'mages'},
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='type',
            field=models.CharField(default=(b'mortal', b'mortal'), max_length=25, verbose_name='Character type', choices=[(b'mortal', b'mortal'), (b'mage', b'mage')]),
            preserve_default=True,
        ),
    ]
