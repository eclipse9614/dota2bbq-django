from django.forms import ModelForm
from dota2bbq.models import Hero, Skill

class HeroForm(ModelForm):
    class Meta:
        model = Hero


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        exclude = ('hero', )