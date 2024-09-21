from django import template

register = template.Library()

@register.filter
def yes_no(value):
    return "Yes" if value else "No"