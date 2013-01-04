from django.forms import ModelForm
from dota2bbq.models import Hero, Skill, Item

class HeroForm(ModelForm):
    class Meta:
        model = Hero


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        exclude = ('hero', )

class ItemForm(ModelForm):
    
    class Meta:
        model = Item
        exclude = ('recipe', )
