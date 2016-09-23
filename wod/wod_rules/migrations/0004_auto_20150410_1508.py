# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mage_rules', '0003_auto_20150410_1508'),
        ('wod_rules', '0003_auto_20150410_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meritprerequisiteskill',
            name='skill',
            field=models.CharField(max_length=50, verbose_name='Skill', choices=[(b'academics', b'academics'), (b'computer', b'computer'), (b'crafts', b'crafts'), (b'investigation', b'investigation'), (b'medicine', b'medicine'), (b'occult', b'occult'), (b'politics', b'politics'), (b'science', b'science'), (b'athletics', b'athletics'), (b'brawl', b'brawl'), (b'drive', b'drive'), (b'firearms', b'firearms'), (b'larceny', b'larceny'), (b'stealth', b'stealth'), (b'survival', b'survival'), (b'weaponry', b'weaponry'), (b'animal_ken', b'animal_ken'), (b'empathy', b'empathy'), (b'expression', b'expression'), (b'intimidation', b'intimidation'), (b'persuasion', b'persuasion'), (b'socialize', b'socialize'), (b'streetwise', b'streetwise'), (b'subterfuge', b'subterfuge')]),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
    ]
