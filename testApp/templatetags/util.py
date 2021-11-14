from django import template

register = template.Library()


@register.filter
def get_type(value):
    return type(value)


@register.filter
def get_vars(value):
    return vars(value)