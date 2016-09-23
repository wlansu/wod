# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wod_rules', '0002_auto_20150410_1125'),
        ('characters', '0002_auto_20141023_2053'),
    ]

    operations = [
        migrations.CreateModel(
            name='MageNPC',
            fields=[
                ('magecharacter_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='characters.MageCharacter')),
                ('player_description', models.TextField(help_text='Players can add their own description for this character.', null=True, verbose_name='Description', blank=True)),
                ('gm_notes', models.TextField(help_text='Special notes visible only to the GM', null=True, verbose_name='Description', blank=True)),
            ],
            options={
                'verbose_name_plural': "mage npc's",
            },
            bases=('characters.magecharacter',),
        ),
        migrations.RenameField(
            model_name='magecharacter',
            old_name='user',
            new_name='player',
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='academics',
            field=models.IntegerField(default=0, verbose_name='Academics', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='age',
            field=models.IntegerField(default=21, verbose_name='Age'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='animal_ken',
            field=models.IntegerField(default=0, verbose_name='Animal_ken', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='arcane_xp',
            field=models.IntegerField(null=True, verbose_name='Arcane experience points', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='armor',
            field=models.IntegerField(default=0, verbose_name='Armor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='athletics',
            field=models.IntegerField(default=0, verbose_name='Athletics', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='brawl',
            field=models.IntegerField(default=0, verbose_name='Brawl', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='composure',
            field=models.IntegerField(default=1, verbose_name='Composure', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='computer',
            field=models.IntegerField(default=0, verbose_name='Computer', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='crafts',
            field=models.IntegerField(default=0, verbose_name='Crafts', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='death',
            field=models.IntegerField(default=0, verbose_name='Death', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='defense',
            field=models.IntegerField(default=0, verbose_name='Defense'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='description',
            field=models.TextField(help_text='A description of your character.', null=True, verbose_name='Description', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='dexterity',
            field=models.IntegerField(default=1, verbose_name='Dexterity', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='drive',
            field=models.IntegerField(default=0, verbose_name='Drive', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='empathy',
            field=models.IntegerField(default=0, verbose_name='Empathy', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='expression',
            field=models.IntegerField(default=0, verbose_name='Expression', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='fate',
            field=models.IntegerField(default=0, verbose_name='Fate', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='firearms',
            field=models.IntegerField(default=0, verbose_name='Firearms', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='forces',
            field=models.IntegerField(default=0, verbose_name='Forces', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='gnosis',
            field=models.IntegerField(blank=True, null=True, verbose_name='Gnosis', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='health',
            field=models.IntegerField(default=0, verbose_name='Health'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='initiative',
            field=models.IntegerField(default=0, verbose_name='Initiative modifier'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='intelligence',
            field=models.IntegerField(default=1, verbose_name='Intelligence', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='intimidation',
            field=models.IntegerField(default=0, verbose_name='Intimidation', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='investigation',
            field=models.IntegerField(default=0, verbose_name='Investigation', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='larceny',
            field=models.IntegerField(default=0, verbose_name='Larceny', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='life',
            field=models.IntegerField(default=0, verbose_name='Life', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='manipulation',
            field=models.IntegerField(default=1, verbose_name='Manipulation', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='matter',
            field=models.IntegerField(default=0, verbose_name='Matter', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='medicine',
            field=models.IntegerField(default=0, verbose_name='Medicine', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='mind',
            field=models.IntegerField(default=0, verbose_name='Mind', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='occult',
            field=models.IntegerField(default=0, verbose_name='Occult', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='persuasion',
            field=models.IntegerField(default=0, verbose_name='Persuasion', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='politics',
            field=models.IntegerField(default=0, verbose_name='Politics', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='presence',
            field=models.IntegerField(default=1, verbose_name='Presence', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='prime',
            field=models.IntegerField(default=0, verbose_name='Prime', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='rank_in_order',
            field=models.CharField(help_text='Only needed if you have a specific rank within your order.', max_length=50, null=True, verbose_name='Rank within order', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='resolve',
            field=models.IntegerField(default=1, verbose_name='Resolve', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='science',
            field=models.IntegerField(default=0, verbose_name='Science', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='size',
            field=models.IntegerField(default=0, verbose_name='Size'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='socialize',
            field=models.IntegerField(default=0, verbose_name='Socialize', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='space',
            field=models.IntegerField(default=0, verbose_name='Space', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='speed',
            field=models.IntegerField(default=0, verbose_name='Speed'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='spirit',
            field=models.IntegerField(default=0, verbose_name='Spirit', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='stamina',
            field=models.IntegerField(default=1, verbose_name='Stamina', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='stealth',
            field=models.IntegerField(default=0, verbose_name='Stealth', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='streetwise',
            field=models.IntegerField(default=0, verbose_name='Streetwise', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='strength',
            field=models.IntegerField(default=1, verbose_name='Strength', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='subterfuge',
            field=models.IntegerField(default=0, verbose_name='Subterfuge', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='survival',
            field=models.IntegerField(default=0, verbose_name='Survival', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='time',
            field=models.IntegerField(default=0, verbose_name='Time', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='vice',
            field=models.OneToOneField(default=1, to='wod_rules.Vice'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='virtue',
            field=models.OneToOneField(default=1, to='wod_rules.Virtue'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='weaponry',
            field=models.IntegerField(default=0, verbose_name='Weaponry', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='willpower',
            field=models.IntegerField(default=0, verbose_name='Willpower'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='wisdom',
            field=models.IntegerField(default=7, verbose_name='Wisdom', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='wits',
            field=models.IntegerField(default=1, verbose_name='Wits', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='magecharacter',
            name='xp',
            field=models.IntegerField(null=True, verbose_name='Experience points', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='name',
            field=models.CharField(help_text="Your character's real name.", unique=True, max_length=50, verbose_name='name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='shadow_name',
            field=models.CharField(max_length=50, null=True, verbose_name='Shadow name', blank=True),
            preserve_default=True,
        ),
    ]
