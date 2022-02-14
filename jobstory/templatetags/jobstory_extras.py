from django import template
from django.db.models import Field
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def field_header(context, field, a_class=''):
    sort_field = context['sort_field']
    sort_dir = context['sort_dir']
    arrow = ''
    if sort_field == field.name:
        if sort_dir == '':
            arrow = '&darr;'
        else:
            arrow = '&uarr;'
    return mark_safe(f'{field.verbose_name}{arrow}')


@register.simple_tag
def field_val(obj, field, default=None):
    if isinstance(field, Field):
        val = field.value_from_object(obj)
    else:
        val = getattr(obj, field)
    if val is None:
        val = default
    return val
