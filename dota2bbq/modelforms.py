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

class SkillBuildForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SkillBuildForm, self).__init__(args, kwargs)
        #self.skillNames = self.instance.hero.skill_set.filter(is_main = True).order_by('number').values('name')
        self.fields['build'] = forms.CharField(widget = SkillBuildInput(['1', '2']))

    class Meta:
        model = SkillBuild
