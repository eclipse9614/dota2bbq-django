from eclipse9614 import settings
from django.core.management import setup_environ
setup_environ(settings)
import Queue
from dota2bbq.models import Hero, SkillBuild

for hero in Hero.objects.all():
	skills = hero.skill_set.filter(is_main = True).order_by('number').values_list('id', flat = True)
	initial = [0 for i in range(25)]
	initial[5] = skills[3]
	initial[10] = skills[3]
	initial[15] = skills[3]

	basicskills = Queue.Queue(12)

	for j in range(4):
		for i in range(3):
			basicskills.put(skills[i])

	for i in range(0, 5):
		initial[i] = basicskills.get()

	for i in range(6, 10):
		initial[i] = basicskills.get()

	for i in range(11, 14):
		initial[i] = basicskills.get()

	number = len(hero.skillbuild_set.all()) + 1
	initial = [str(skill) for skill in initial]

	SkillBuild(hero = hero, number = number, build = ','.join(initial)).save()
