# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150421_2037'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wod_rules', '0011_auto_20150421_1653'),
        ('characters', '0017_auto_20150424_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='MortalCharacter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text="Your character's real name.", unique=True, max_length=50, verbose_name='name')),
                ('xp', models.IntegerField(null=True, verbose_name='Experience points', blank=True)),
                ('intelligence', models.IntegerField(default=1, verbose_name='Intelligence', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('wits', models.IntegerField(default=1, verbose_name='Wits', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('resolve', models.IntegerField(default=1, verbose_name='Resolve', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('strength', models.IntegerField(default=1, verbose_name='Strength', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('dexterity', models.IntegerField(default=1, verbose_name='Dexterity', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('stamina', models.IntegerField(default=1, verbose_name='Stamina', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('presence', models.IntegerField(default=1, verbose_name='Presence', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('manipulation', models.IntegerField(default=1, verbose_name='Manipulation', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('composure', models.IntegerField(default=1, verbose_name='Composure', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('description', models.TextField(help_text='A description of your character.', null=True, verbose_name='Description', blank=True)),
                ('age', models.IntegerField(verbose_name='Age')),
                ('type', models.CharField(default=b'mortal', max_length=25, verbose_name='Character type', choices=[(b'mortal', b'Mortal'), (b'mage', b'Mage')])),
                ('is_npc', models.BooleanField(default=False)),
                ('health', models.IntegerField(null=True, verbose_name='Maximum Health', blank=True)),
                ('willpower', models.IntegerField(null=True, verbose_name='Willpower', blank=True)),
                ('size', models.IntegerField(default=5, verbose_name='Size')),
                ('speed', models.IntegerField(null=True, verbose_name='Speed', blank=True)),
                ('initiative', models.IntegerField(null=True, verbose_name='Initiative modifier', blank=True)),
                ('defense', models.IntegerField(null=True, verbose_name='Defense', blank=True)),
                ('armor', models.IntegerField(null=True, verbose_name='Armor', blank=True)),
                ('academics', models.IntegerField(default=0, null=True, verbose_name='Academics', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('computer', models.IntegerField(default=0, null=True, verbose_name='Computer', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('crafts', models.IntegerField(default=0, null=True, verbose_name='Crafts', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('investigation', models.IntegerField(default=0, null=True, verbose_name='Investigation', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('medicine', models.IntegerField(default=0, null=True, verbose_name='Medicine', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('occult', models.IntegerField(default=0, null=True, verbose_name='Occult', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('politics', models.IntegerField(default=0, null=True, verbose_name='Politics', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('science', models.IntegerField(default=0, null=True, verbose_name='Science', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('athletics', models.IntegerField(default=0, null=True, verbose_name='Athletics', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('brawl', models.IntegerField(default=0, null=True, verbose_name='Brawl', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('drive', models.IntegerField(default=0, null=True, verbose_name='Drive', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('firearms', models.IntegerField(default=0, null=True, verbose_name='Firearms', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('larceny', models.IntegerField(default=0, null=True, verbose_name='Larceny', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('stealth', models.IntegerField(default=0, null=True, verbose_name='Stealth', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('survival', models.IntegerField(default=0, null=True, verbose_name='Survival', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('weaponry', models.IntegerField(default=0, null=True, verbose_name='Weaponry', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('animal_ken', models.IntegerField(default=0, null=True, verbose_name='Animal_ken', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('empathy', models.IntegerField(default=0, null=True, verbose_name='Empathy', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('expression', models.IntegerField(default=0, null=True, verbose_name='Expression', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('intimidation', models.IntegerField(default=0, null=True, verbose_name='Intimidation', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('persuasion', models.IntegerField(default=0, null=True, verbose_name='Persuasion', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('socialize', models.IntegerField(default=0, null=True, verbose_name='Socialize', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('streetwise', models.IntegerField(default=0, null=True, verbose_name='Streetwise', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('subterfuge', models.IntegerField(default=0, null=True, verbose_name='Subterfuge', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('morality', models.IntegerField(default=7, verbose_name='Morality', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')])),
            ],
            options={
                'ordering': ('-name',),
                'verbose_name': 'mortal',
                'verbose_name_plural': 'mortals',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MortalNPC',
            fields=[
                ('mortalcharacter_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='characters.MortalCharacter')),
                ('player_description', models.TextField(help_text='Players can add their own description for this character.', null=True, verbose_name='Description', blank=True)),
                ('gm_notes', models.TextField(help_text='Special notes visible only to the GM', null=True, verbose_name='Description', blank=True)),
            ],
            options={
                'verbose_name_plural': "mortal npc's",
            },
            bases=('characters.mortalcharacter',),
        ),
        migrations.AddField(
            model_name='mortalcharacter',
            name='campaign',
            field=models.ForeignKey(to='users.Campaign'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mortalcharacter',
            name='player',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mortalcharacter',
            name='vice',
            field=models.ForeignKey(to='wod_rules.Vice'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mortalcharacter',
            name='virtue',
            field=models.ForeignKey(to='wod_rules.Virtue'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='magecharacter',
            name='campaign',
            field=models.ForeignKey(to='users.Campaign'),
            preserve_default=True,
        ),
    ]
