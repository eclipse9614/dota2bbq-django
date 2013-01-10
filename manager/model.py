from manager.fields import SkillBuildField

class SkillBuildModelField(models.Field):

	def formfield(self, **kwargs):
		return super(SkillBuildModelField, self).formfield(form_class = SkillBuildField, **kwargs)

	def get_internal_type(self):
		return 'CommaSeparatedIntegerField'
