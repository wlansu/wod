# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('characters', '0014_magecharacter_is_npc'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='magecharacter',
            options={'ordering': ('-shadow_name', '-name'), 'verbose_name': 'mage', 'verbose_name_plural': 'mages'},
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='campaign',
            field=models.ForeignKey(related_name='character', blank=True, to='users.Campaign', null=True),
            preserve_default=True,
        ),
    ]
