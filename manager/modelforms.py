import Queue
from django import forms
from dota2bbq.models import Hero, Skill, Item, SkillBuild
from manager.fields import SkillBuildField

class HeroForm(forms.ModelForm):
    class Meta:
        model = Hero


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        exclude = ('hero', )

class ItemForm(forms.ModelForm):
    
    class Meta:
        model = Item
        exclude = ('recipe', )

def GenereateSkillBuildForm(mainSkills):
    """Because we need initial values for skillChoices, but we cannot use __init__ function Because
    When use inline formset u can only assign a class not an instance to it, thus, we have to Genereat
    a dynamic class for inlineform set"""
    class SkillBuildForm(forms.ModelForm):
        # print mainSkills
        mainSkills.append((0, u'Stats')) # add stats for all heroes
        # generate basic skill build pattern here as initial
        initial = [0 for i in range(25)]
        # ultimates
        initial[5] = mainSkills[3][0]
        initial[10] = mainSkills[3][0]
        initial[15] = mainSkills[3][0]
        #basic skills
        basicSkills = Queue.Queue(12)

        for j in range(4):
            for i in range(3):
                basicSkills.put(mainSkills[i][0])

        for i in range(0, 5):
            initial[i] = basicSkills.get()

        for i in range(6, 10):
            initial[i] = basicSkills.get()

        for i in range(11, 14):
            initial[i] = basicSkills.get()

        build = SkillBuildField(choices = mainSkills, initial = initial) #initial all the slots to be stats
        class Meta:
            model = SkillBuild

    return SkillBuildForm