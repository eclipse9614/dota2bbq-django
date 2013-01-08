from django import forms
from dota2bbq.widgets import SkillBuildInput

class SkillBuildField(forms.MultiValueField):
	def __init__(self, choices = [], **kwargs):
		_fields = [forms.CharField() for i in range(25)]
		_widget = SkillBuildInput(choices)
		super(SkillBuildField, self).__init__(widget = _widget, fields = _fields, **kwargs)


	def compress(self, data_list):
		if data_list:
			return ','.join(data_list)
		return "None"
