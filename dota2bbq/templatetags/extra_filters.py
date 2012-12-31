from django import template

register = template.Library()


@register.filter(name='spaces2underscores')
def spaces2underscores(value):
    return value.replace(' ', '_')


