from django import template

register = template.Library()


@register.filter
def getvalue(obj, key):
    return getattr(obj, key)
