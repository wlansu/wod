# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('mage_rules', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='magecharacter',
            name='order',
            field=models.ForeignKey(blank=True, to='mage_rules.Order', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='path',
            field=models.ForeignKey(to='mage_rules.Path'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
