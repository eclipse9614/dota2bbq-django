from django import forms
from dota2bbq.models import Hero, Skill, Item, SkillBuild
from dota2bbq.widgets import SkillBuildInput

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
    class SkillBuildForm(forms.ModelForm):
        print mainSkills
        skillChoices = [(skill['id'], skill['name']) for skill in mainSkills]
        skillChoices.append(('0', 'Stats'))
        build = forms.CharField(widget = SkillBuildInput(skillChoices))
        class Meta:
            model = SkillBuild
    return SkillBuildForm