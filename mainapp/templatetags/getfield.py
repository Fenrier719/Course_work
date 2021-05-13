from django import template

register = template.Library()

@register.filter
def getfield(obj, value):
    return getattr(obj, value)