from django import template

register = template.Library()

@register.simple_tag
def nav_active(a,b):
    if a == b:
        return 'class="active"'
