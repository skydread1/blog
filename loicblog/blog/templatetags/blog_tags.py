from django import template
from django.utils.html import mark_safe
from ..models import Category

register = template.Library()

@register.simple_tag
def get_categories():
    categories = Category.objects.all()
    return categories

@register.filter
def highlight_text(value, search_term):
    search_term_upper = search_term.upper()
    value_upper = value.upper()
    highlighted = value_upper.replace(search_term_upper, f'<span class="highlight-text">{search_term_upper}</span>')
    return mark_safe(highlighted)
