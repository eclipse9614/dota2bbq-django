from django.db import models

class Hero(models.Model):
	FACTIONS = (
		('RA', 'Radient'),
		('DI', 'Dire'),
		('NE', 'Netural')
	)

	CLASSES = (
		("STR", 'Strength'),
		("AGI", 'Agility'),
		("INT", 'Intelligence')
	)
	name = models.CharField(max_length = 30)
	faction = models.CharField(max_length = 2, choices = FACTIONS)
	specialty = models.CharField(max_length = 3, choices = CLASSES)
	lore = models.TextField()
	basic_str = models.PositiveSmallIntegerField()
	basic_agi = models.PositiveSmallIntegerField()
	basic_int = models.PositiveSmallIntegerField()
	str_inc = models.FloatField()
	agi_inc = models.FloatField()
	int_inc = models.FloatField()
	movement = models.PositiveSmallIntegerField()
	armor = models.FloatField()
	min_dmg = models.PositiveSmallIntegerField()
	max_dmg = models.PositiveSmallIntegerField()

	def __unicode__(self):
		return self.name


class Item(models.Model):
	TYPES = (
		(1, 'Consumables'),
		(2, "Attributes"),
		(3, "Armaments"),
		(4, 'Arcane'),
		(5, 'Common'),
		(6, 'Support'),
		(7, 'Caster'),
		(8, 'Weapons'),
		(9, 'Armor'),
		(10, 'Artifacts'),
		(11, 'Secret Shop'),
		(0, 'Hidden'),
	)

	name =  models.CharField(max_length = 30)
	description = models.TextField()
	cost = models.SmallIntegerField()
	usage = models.TextField(blank = True)
	attributes = models.TextField(blank = True)
	kind = models.PositiveSmallIntegerField(choices = TYPES)
	recipe = models.ManyToManyField('self', blank = True, symmetrical=False, through='Composition')

	def __unicode__(self):
		return self.name

	@classmethod
	def get_kinds_display(cls):
		return cls.TYPES


class Composition(models.Model):
	whole = models.ForeignKey(Item, related_name = 'as_a_whole')
	component = models.ForeignKey(Item, related_name = 'as_a_part')


class Skill(models.Model):
	hero = models.ForeignKey(Hero)
	number = models.PositiveSmallIntegerField()
	name = models.CharField(max_length = 30)
	description = models.TextField()
	activity = models.BooleanField()
	mana_cost = models.TextField(blank = True, null = True)
	cooldown = models.TextField(blank = True, null = True)

	def __unicode__(self):
		return self.name