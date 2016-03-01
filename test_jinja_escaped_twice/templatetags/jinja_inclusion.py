from django import template
from django.template.loader import get_template

register = template.Library()

t = get_template('inclusion_template.jinja2')


@register.inclusion_tag('inclusion_template.jinja2')
def include_jinja():
    return {}


@register.inclusion_tag(t)
def include_jinja_alt():
    return {}
