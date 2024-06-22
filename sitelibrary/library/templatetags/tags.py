from django import template
from library import views

register = template.Library()


@register.simple_tag()
def get_genres():
    return views.list_genre
