from django import template

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
    """Умножает value на arg."""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return None