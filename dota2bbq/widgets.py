from django.forms import widgets



class SkillBuildInput(widgets.MultiWidget):
    """
        This is a custom widget for the hero's skill build input
        Since hero has 25 levels, this widget has 25 select widget as its componets
        each select widget has 5 skill choices to choose from, four mains skills, and one for stats(except invoker)
    """
    def __init__(self, skillchoices, attrs = None):
        
        _widgets = [widgets.Select(attrs = attrs, choices = skillchoices) for i in range(25)]

        super(SkillBuildInput, self).__init__(_widgets, attrs)


    def decompress(self, value):
        """ 
            this method is used to combine values from 25 widgets into one value
            because I have separatedintegerfield for skillbuild so convert the 25 values into one legit value for this field
            if None, return 25 Nones 
        """
        if value:
            skillsbuild = value.split(',')
            return [skill for skill in skillsbuild]
        else:
            return [None for i in range(25)]


    def format_output(self, rendered_widgets):
        return u'<br>'.join(rendered_widgets)