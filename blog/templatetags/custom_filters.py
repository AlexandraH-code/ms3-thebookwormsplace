from django import template

register = template.Library()

@register.filter
def to_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return 0


@register.filter
def to(value, arg):
    """
    Usage: {% for i in 1|to:6 %} loops over 1 to 5
    """
    return range(int(value), int(arg))


@register.filter
def floatval(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0.0