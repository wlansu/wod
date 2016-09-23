# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wod_rules', '0009_auto_20150416_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialty',
            name='skill',
            field=models.CharField(max_length=25, verbose_name='Skill', choices=[(b'academics', b'Academics'), (b'computer', b'Computer'), (b'crafts', b'Crafts'), (b'investigation', b'Investigation'), (b'medicine', b'Medicine'), (b'occult', b'Occult'), (b'politics', b'Politics'), (b'science', b'Science'), (b'athletics', b'Athletics'), (b'brawl', b'Brawl'), (b'drive', b'Drive'), (b'firearms', b'Firearms'), (b'larceny', b'Larceny'), (b'stealth', b'Stealth'), (b'survival', b'Survival'), (b'weaponry', b'Weaponry'), (b'animal_ken', b'Animal_ken'), (b'empathy', b'Empathy'), (b'expression', b'Expression'), (b'intimidation', b'Intimidation'), (b'persuasion', b'Persuasion'), (b'socialize', b'Socialize'), (b'streetwise', b'Streetwise'), (b'subterfuge', b'Subterfuge')]),
            preserve_default=True,
        ),
    ]
