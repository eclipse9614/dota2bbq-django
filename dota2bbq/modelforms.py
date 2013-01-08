from django import forms
from dota2bbq.models import Hero, Skill, Item, SkillBuild
from dota2bbq.fields import SkillBuildField

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
        mainSkills.append((0, 'Stats')) # add stats for all heroes
        build = SkillBuildField(choices = mainSkills, initial = [0 for i in range(25)]) #initial all the slots to be stats
        class Meta:
            model = SkillBuild

    return SkillBuildForm