from django import template

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
    """Умножает value на arg."""
    try:
        total = value * arg
        return round(total, 2)
    except (ValueError, TypeError):
        return None