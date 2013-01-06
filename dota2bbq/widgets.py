from django.forms import widgets


class SkillBuildInput(widgets.MultiWidget):
    """docstring for SkillBuildInput"""
    def __init__(self, skillnumbers, attrs = None):
        _widgets = (
                widgets.Select(attrs = attrs, choices = skillnumbers),
                widgets.Select(attrs = attrs, choices = skillnumbers),
                widgets.Select(attrs = attrs, choices = skillnumbers),
                widgets.Select(attrs = attrs, choices = skillnumbers),
                widgets.Select(attrs = attrs, choices = skillnumbers),
                widgets.Select(attrs = attrs, choices = skillnumbers),
                widgets.Select(attrs = attrs, choices = skillnumbers),
                widgets.Select(attrs = attrs, choices = skillnumbers),
                widgets.Select(attrs = attrs, choices = skillnumbers),
                widgets.Select(attrs = attrs, choices = skillnumbers),
                widgets.Select(attrs = attrs, choices = skillnumbers),
                widgets.Select(attrs = attrs, choices = skillnumbers),
                widgets.Select(attrs = attrs, choices = skillnumbers),
                widgets.Select(attrs = attrs, choices = skillnumbers),
                widgets.Select(attrs = attrs, choices = skillnumbers),
                widgets.Select(attrs = attrs, choices = skillnumbers),
                widgets.Select(attrs = attrs, choices = skillnumbers),
                widgets.Select(attrs = attrs, choices = skillnumbers),
                widgets.Select(attrs = attrs, choices = skillnumbers),
                widgets.Select(attrs = attrs, choices = skillnumbers),
                widgets.Select(attrs = attrs, choices = skillnumbers),
                widgets.Select(attrs = attrs, choices = skillnumbers),
                widgets.Select(attrs = attrs, choices = skillnumbers),
                widgets.Select(attrs = attrs, choices = skillnumbers),
                widgets.Select(attrs = attrs, choices = skillnumbers),
                widgets.Select(attrs = attrs, choices = skillnumbers),
            )
        super(SkillBuildInput, self).__init__(_widgets, attrs)

    def decompress(self, value):
        if value:
            skillsbuild = value.split(',')
            return [skill for skill in skillsbuild]
        else:
            return [None for i in range(25)]