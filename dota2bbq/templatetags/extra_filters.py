from django import template

register = template.Library()


@register.filter(name='spaces2underscores')
def spaces2underscores(value):
    return value.replace(' ', '_')

@register.filter(name='removeapostrophe')
def removeapostrophe(value):
	return value.replace("'", "")
