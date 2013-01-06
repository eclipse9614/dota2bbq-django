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
	is_main = models.BooleanField(default = True)

	def __unicode__(self):
		return self.name


	def clean(self):
		from django.core.exceptions import ValidationError
		try:
			self.hero.skill_set.exclude(id = self.id).get(number = self.number)
			raise ValidationError('This skill number is used, please use another one')
		except Skill.DoesNotExist:
			pass



class SkillBuild(models.Model):
	hero = models.ForeignKey(Hero)
	number = models.PositiveSmallIntegerField()
	build = models.CommaSeparatedIntegerField(max_length = 100)

	def clean(self):
		from django.core.exceptions import ValidationError
		#here, check whether the number attribtue is right or wrong
		try:
			self.hero.skillbuild_set.exclude(id = self.id).get(number = self.number)
			raise ValidationError('This skill build number is used, please use another one')
		except SkillBuild.DoesNotExist:
			pass

		#here, check whether the build attribute is right or wrong
		skills_order = self.build.split(',')
		#make sure there are 25 skills in the build
		if len(skills_order) != 25:
			raise ValidationError('A skill build needs 25 steps.')
		skills_order = [int(step) for step in skills_order]
		#make sure that in one build, there are ten stats build or not at all(invoker)
		#0 means stat
		stats_count = skills_order.count(0)
		#this is the main skills that are upgradable for each hero
		upgradable_skills = self.hero.skill_set.filter(is_main = True).order_by('number').values('number')
		skill_counts = [skills_order.count(skill.number) for skill in upgradable_skills]

		if len(skill_counts) != 4:
			raise ValidationError('Each Hero has only four upgradable skills')

		if self.hero.name == 'Invoker':
			if stats_count != 0:
				raise ValidationError('Invoker has no stats build')
			if skill_counts != [7, 7, 7, 4]:
				raise ValidationError('Wrong skill distribution for invoker')
		else:
			if stats_count != 10:
				raise ValidationError('A hero should have 10 stats build')
			if skill_counts != [4, 4, 4, 3]:
				raise ValidationError('Wrong skill distribution for this hero')


