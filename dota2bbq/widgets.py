from django.forms import widgets


class SkillBuildInput(widgets.MultiWidget):
    """docstring for SkillBuildInput"""
    def __init__(self, skillchoices, attrs = None):

        _widgets = (
                widgets.Select(attrs = attrs, choices = skillchoices),
                widgets.Select(attrs = attrs, choices = skillchoices),
                widgets.Select(attrs = attrs, choices = skillchoices),
                widgets.Select(attrs = attrs, choices = skillchoices),
                widgets.Select(attrs = attrs, choices = skillchoices),
                widgets.Select(attrs = attrs, choices = skillchoices),
                widgets.Select(attrs = attrs, choices = skillchoices),
                widgets.Select(attrs = attrs, choices = skillchoices),
                widgets.Select(attrs = attrs, choices = skillchoices),
                widgets.Select(attrs = attrs, choices = skillchoices),
                widgets.Select(attrs = attrs, choices = skillchoices),
                widgets.Select(attrs = attrs, choices = skillchoices),
                widgets.Select(attrs = attrs, choices = skillchoices),
                widgets.Select(attrs = attrs, choices = skillchoices),
                widgets.Select(attrs = attrs, choices = skillchoices),
                widgets.Select(attrs = attrs, choices = skillchoices),
                widgets.Select(attrs = attrs, choices = skillchoices),
                widgets.Select(attrs = attrs, choices = skillchoices),
                widgets.Select(attrs = attrs, choices = skillchoices),
                widgets.Select(attrs = attrs, choices = skillchoices),
                widgets.Select(attrs = attrs, choices = skillchoices),
                widgets.Select(attrs = attrs, choices = skillchoices),
                widgets.Select(attrs = attrs, choices = skillchoices),
                widgets.Select(attrs = attrs, choices = skillchoices),
            )
        super(SkillBuildInput, self).__init__(_widgets, attrs)

    def decompress(self, value):
        if value:
            skillsbuild = value.split(',')
            return [skill for skill in skillsbuild]
        else:
            return [None for i in range(25)]


    def format_output(self, rendered_widgets):
        return u''.join(rendered_widgets)


    def value_from_datadict(self, data, files, name):
        skillList = [widget.value_from_datadict(data, files, name + '_%s' % i) for i, widget in enumerate(self.widgets)]
        if skillList.count(None) == 25:
            return ''
        return ','.join(skillList)